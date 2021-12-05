import sqlite3
import pyedflib
from data_fetching.config import Config
from data_fetching.utils import sql

from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults



class ValidateData(BaseOperator):
    @apply_defaults
    def __init__(self, **kwargs):
        super(ValidateData, self).__init__(**kwargs)

        self.metadata_conn = None

    def meta_db_connect(self):
        return sqlite3.connect(Config.recording_db_path, check_same_thread=False)
    
    def close_conn(self):
        if self.metadata_conn is not None:
            self.metadata_conn.close()

    def read_use_pyedflib(self, edf_path, chn=0):
        f = pyedflib.EdfReader(edf_path)
        sigbufs = f.readSignal(chn=chn)
        f._close()
        return sigbufs

    def read_use_byte(self, edf_path, ch=0):
        byte_data = None
        with open(edf_path, "rb") as f:
            byte_data = f.read()

        n_signals = int(byte_data[252:256].decode('ascii').strip())
        duration = float(byte_data[244:252].decode('ascii').strip())
        n_samples_start = 256 + (216*n_signals)
        n_samples_end = n_samples_start+8
        n_samples = int(byte_data[n_samples_start:n_samples_end].decode('ascii').strip())
        record_start_idx = 256+(n_signals*256)

        return byte_data[record_start_idx+ch::n_signals], n_samples, duration


    def check_ecgtest_data(self):
        metadata_cur = self.metadata_conn.cursor()
        metadata_cur.execute(sql.q_get_ecgtest())
        ecgtests = metadata_cur.fetchall()

        diff_len_list = []
        for id, seq, org_id, site_id, region, edf_path in ecgtests:
            signal_from_pyedflib = self.read_use_pyedflib(edf_path)
            signal_len_from_pyedflib = len(signal_from_pyedflib)

            signal_from_bytedata, n_samples, duration = self.read_use_byte(edf_path)
            signal_len_from_bytedata = ((len(signal_from_bytedata)/2)/n_samples) * duration

            if float(signal_len_from_pyedflib) != float(signal_len_from_bytedata):
                diff_len_list.append([id, seq, org_id, site_id, region])

        print(f"Different Length data num is : {len(diff_len_list)}")
        print(f"List is : {diff_len_list}")

        metadata_cur.close()


    def execute(self, context):
        self.metadata_conn = self.meta_db_connect()

        self.check_ecgtest_data()

        self.close_conn()

        return 1

