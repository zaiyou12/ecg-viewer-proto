import mysql.connector
import numpy as np
import json
from datetime import timedelta
import sqlite3
import os

from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults
from data_fetching.utils import sql
from data_fetching.utils.custom_edf import EDFhandler
from data_fetching.config import Config
from data_fetching.utils.exception_custom import Fetching_Error



class FetchingData(BaseOperator):
    @apply_defaults
    def __init__(self, user, password, host, port, database, region, get_type, **kwargs):
        super(FetchingData, self).__init__(**kwargs)
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.database = database
        self.region = region
        self.get_type = get_type   # 현재는 'all'만

        self.conn = None
        self.metadata_conn = None

    def meta_db_connect(self):
        return sqlite3.connect(Config.recording_db_path, check_same_thread=False)


    def db_connect(self):
        # return mysql.connector.connect(user=self.user, password=self.password, host=self.host, port=self.port, database=self.database)
        return mysql.connector.connect(user='master', password=self.password, host=self.host, port=self.port, database=self.database)

    def close_conn(self):
        if self.conn is not None:
            self.conn.close()
        
        if self.metadata_conn is not None:
            self.metadata_conn.close()

    # blob 재배치 한 ID에 두개 이상있을때 만
    def replace_data_and_merge(self, header_dump, signal_header_dump, datetime_dump, signal_dump, n_samples):
        if len(datetime_dump)<2:
            return -1
        datetime_arr = np.array(datetime_dump)
        sort_index = np.argsort(datetime_arr)
        # Byte Data 병합
        merge_data = signal_dump[sort_index[0]]  # byte array
        zero_two_byte = b'\x00\x00'   # For Padding
        # 날짜 순대로 데이터 병합
        for idx in range(len(sort_index)-1):
            # Get Datetime
            now_datetime = datetime_arr[sort_index[idx]]
            next_datetime = datetime_arr[sort_index[idx+1]]
            # Add Byte
            now_signal_len_in_second = int( len(signal_dump[sort_index[idx]])/(n_samples*2*2) )
            between_start_time = int((next_datetime-now_datetime).total_seconds())
            merge_data += zero_two_byte*n_samples*2*(between_start_time-now_signal_len_in_second)
            merge_data += signal_dump[sort_index[idx+1]]

        # 대표 Header
        merged_header = header_dump[sort_index[0]]
        merged_signal_header = signal_header_dump[sort_index[0]]
        merged_startdate = datetime_arr[sort_index[0]]
        return merged_header, merged_signal_header, merged_startdate, merge_data

    def get_blob_data_merged(self, blob_list):
        # For data collecting
        datetime_dump = []
        signal_dump = []
        header_dump = []
        signal_header_dump = []
        n_samples=None
        for id, blob in blob_list:
            edfhandler = EDFhandler()
            edfhandler.read_blob(blob)
            if edfhandler.check_data_status() == -1:
                print("Erro data")
                del edfhandler
                continue
            # 첫번째 채널의 신호 및 날짜 정보, header, signal header 가져오기
            signal_in_byte = edfhandler.get_signal(0, False)
            blob_datetime = edfhandler.get_start_datetime()
            datetime_dump.append(blob_datetime)
            signal_dump.append(signal_in_byte)
            header_dump.append(edfhandler.return_header())
            signal_header_dump.append(edfhandler.return_signal_header())
            n_samples = int(edfhandler.get_info_from_signalheader('n_samples',0))
            del edfhandler
        if len(datetime_dump)>2:
            merged_header, merged_signal_header, merged_startdate, merge_data = self.replace_data_and_merge(header_dump, signal_header_dump, datetime_dump, signal_dump, n_samples)
            return merged_header, merged_signal_header, merged_startdate, merge_data, n_samples

        elif len(datetime_dump) == 0:
            return -1, -1, -1, -1, -1

        else:
            merge_data = signal_dump[0]
            # 대표 Header
            merged_header = header_dump[0]
            merged_signal_header = signal_header_dump[0]
            merged_startdate = datetime_dump[0]
            return merged_header, merged_signal_header, merged_startdate, merge_data, n_samples

    ####################
    ##### 개별 테스트에 저장 및 metadata 저장
    def save_files(self, region, test_id, test_seq, rec_start, dur, org_id, site_id):
        cur = self.conn.cursor(buffered=False)
        # Blob 가져오기
        query = sql.q_get_blob_data(test_id)
        cur.execute(query)
        blob_list = cur.fetchall()
        cur.close()
        # Blob에서 Merging
        merged_header, merged_signal_header, merged_startdate, merge_data, n_samples  = self.get_blob_data_merged(blob_list)

        if merged_header == -1:
            return -1
            
        # For duration
        merge_dur_in_second = len(merge_data) / 512

        # Create EDF File
        # create_merged_edf
        edfhandler = EDFhandler()
        edfhandler.set_header(merged_header)
        edfhandler.set_signal_header(merged_signal_header)
        edfhandler.set_record_data(merge_data)
        # change header
        edfhandler.change_datetime_header(merged_startdate)
        edfhandler.change_header('n_records', str(int(len(merge_data)/(n_samples*2))))
        # merge edf & save edf
        edf_dir = os.path.join(Config.save_data_base_path, region, str(org_id), str(site_id))
        if not os.path.exists(edf_dir):
            os.makedirs(edf_dir)
        edf_path = os.path.join(edf_dir, test_seq+".edf")

        try:
            edfhandler.save_edf_format(edf_path)
        except Exception as e:
            raise Fetching_Error(f"EDF Save Failed --> {e}")

        # Delete object
        del edfhandler

        # Json Metadata
        dur_hour, remainder = divmod(merge_dur_in_second, 3600)
        dur_min, dur_sec = divmod(remainder, 60)
        details_path = os.path.join(edf_dir, test_seq+".json")

        try:
            with open(details_path, 'w') as json_file:
                details_json = {
                    'start_time': merged_startdate.strftime('%Y-%m-%d:%H:%M:%S'),
                    'actual_duration': '{:02}:{:02}:{:02}'.format(int(dur_hour), int(dur_min), int(dur_sec))
                }
                json.dump(details_json, json_file)
        except Exception as e:
            raise Fetching_Error(f"Details Save Failed --> {e}") 

        # Meta data 저장 및 Commit
        for_unique_check = f"{region}_{org_id}_{site_id}_{test_seq}"
        metadata_cur = self.metadata_conn.cursor()
        try:
            metadata_cur.execute(sql.q_insert_metadata(seq=test_seq, org_id=org_id, site_id=site_id, region=region, duration=dur, edf_path=edf_path, details_path=details_path, for_unique=for_unique_check))
        except Exception as e:
            metadata_cur.close()
            raise Fetching_Error(f"MetaData Save Failed --> {e}") 
        metadata_cur.close()
        self.metadata_conn.commit()

        return 0


    ####################
    ##### 현재 DB에 있는 모든 ECGTest 저장
    def getdata_all(self):
        cur = self.conn.cursor(buffered=False)
        
        cur.execute(sql.q_get_test_all())
        ecgtests = cur.fetchall()
        cur.close()
        failed_list=[]
        for test_id, test_seq, rec_start, dur, org_id, site_id in ecgtests:
            try:
                self.save_files(region=self.region, test_id=test_id, test_seq=test_seq, rec_start=rec_start, dur=self.categorize_by_dur(dur), org_id=org_id, site_id=site_id)
            except Exception as e:
                print(f"Error!!! {test_id} -> ", e)
                failed_list.append(test_id)

        print(f"Failed Num is -> {len(failed_list)}")
        print(f"Failed List is -> {failed_list}")


    ####################
    ##### 특정 조건 아래에서만
    def getdata_with_constraind(self, org_id, site_id, test_sec):
        cur = self.conn.cursur(buffered=False)
        cur.execute(sql.q_get_test_with_constraint(org_id, site_id, test_sec))
        ecgtests = cur.fetchall()
        cur.close()
        failed_list=[]
        for test_id, test_seq, rec_start, dur, org_id, site_id in ecgtests:
            try:
                self.save_files(region=self.region, test_id=test_id, test_seq=test_seq, rec_start=rec_start, dur=self.categorize_by_dur(dur), org_id=org_id, site_id=site_id)
            except Exception as e:
                print(f"Error!!! {test_id} -> ", e)
                failed_list.append(test_id)

        print(f"Failed Num is -> {len(failed_list)}")
        print(f"Failed List is -> {failed_list}")



    def execute(self, context):
        self.conn = self.db_connect()
        self.metadata_conn = self.meta_db_connect()

        config_dict = context["dag_run"].conf()
        org_id = config_dict["org_id"]
        site_id = config_dict["sit_id"]
        test_sec = config_dict["sec"]
        if org_id is None and site_id is None and test_sec is None:
            # 조건 없이
            self.getdata_all()
        else:
            # 조건 하나라도 있을 시
            

            




        if self.get_type == 'all':
            self.getdata_all()

        self.close_conn()
        return 1


    def categorize_by_dur(self, dur):
        if dur is None:
            return 'undefined'
        dur = int(dur)
        if dur < 0:
            return 'undefined'
        elif dur < 2:
            return '2'
        elif dur < 24:
            return '24'
        elif dur < 48:
            return '48'
        else:
            return '72'




################################################################################################################
################################################################################################################

class Copy_Org_Site(BaseOperator):
    @apply_defaults
    def __init__(self, user, password, host, port, database, region, **kwargs):
        super(Copy_Org_Site, self).__init__(**kwargs)
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.database = database
        self.region = region

        self.conn = None
        self.metadata_conn = None


    def meta_db_connect(self):
        return sqlite3.connect(Config.recording_db_path, check_same_thread=False)

    def db_connect(self):
        # return mysql.connector.connect(user=self.user, password=self.password, host=self.host, port=self.port, database=self.database)
        return mysql.connector.connect(user='master', password=self.password, host=self.host, port=self.port, database=self.database)


    def execute(self, context):
        self.conn = self.db_connect()
        self.metadata_conn = self.meta_db_connect()

        self.copy_org_info()
        self.copy_site_info()

        self.close_conn()

        return 1
        

    def copy_org_info(self):
        cur = self.conn.cursor(buffered=False)
        cur.execute(sql.q_get_org_info())
        org_info_lists = cur.fetchall()
        cur.close()

        metadata_cur = self.metadata_conn.cursor()
        for org_id, org_code, org_name in org_info_lists:
            metadata_cur.execute(sql.q_check_in_org(org_id=org_id))
            check_list = metadata_cur.fetchall()

            if len(check_list) == 0:
                metadata_cur.execute(sql.q_insert_to_org(org_id=org_id, org_code=org_code, org_name=org_name))

        metadata_cur.close()
        self.metadata_conn.commit()

    
    def copy_site_info(self):
        cur = self.conn.cursor(buffered=False)
        cur.execute(sql.q_get_site_info())
        site_info_lists = cur.fetchall()
        cur.close()

        metadata_cur = self.metadata_conn.cursor()
        for site_id, site_code, site_name in site_info_lists:
            metadata_cur.execute(sql.q_check_in_site(site_id=site_id))
            check_list = metadata_cur.fetchall()

            if len(check_list) == 0:
                metadata_cur.execute(sql.q_insert_to_site(site_id=site_id, site_code=site_code, site_name=site_name))

        metadata_cur.close()
        self.metadata_conn.commit()

    
    def close_conn(self):
        if self.conn is not None:
            self.conn.close()
        
        if self.metadata_conn is not None:
            self.metadata_conn.close()






