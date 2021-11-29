from flask import jsonify, request, url_for, current_app
import math
import os
import sys

from numpy.lib.type_check import imag

from app import db
from . import ecgtest
from . import query
from .utils import get_details, get_ecg_data, signal_plot_to_png, file_exist_check

# 초기 파일 경로 추가
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))
from preprocess.pre_class import process_module



one_image_len = 256 * 10   # hz x 1min
len_per_page = one_image_len * 6   # one_image_len x 6images    

#########################################################################################################
##### ECGTest List Main View
# Return ECG Test List & Info
#########################################################################################################
@ecgtest.route('/ecgtest', methods=['GET'])
def get_ecgtests():
    
    if_testgroup_selected = False

    page = request.args.get('page', 1, type=int)
    # For Filter
    durations = request.args.getlist('duration', type=str)
    regions = request.args.getlist('region', type=str)
    conditions = request.args.getlist('condition', type=str)
    test_groups = request.args.getlist('test_group', type=int)
    # For Others
    others = request.args.get('query', type=str)
    qu = query.q_get_ecgtests(durations=durations, regions=regions, conditions=conditions, test_groups=test_groups, others=others)
    # print(f"SQL QUERY IS : {qu}")
    cur = db.cursor()
    cur.execute(qu)
    ecgtest_list = [dict(row) for row in cur.fetchall()]
    cur.close()
    db.commit()

    # Page Cal
    total_data_num = len(ecgtest_list)
    per_page = 15
    total_page = math.ceil(float(total_data_num)/per_page)
    ecgtest_list = ecgtest_list[(page-1)*per_page:page*per_page]

    if len(test_groups)>=1:
        if_testgroup_selected = True
    res = {
        "tests": ecgtest_list,
        "page": page,
        "total_page": total_page,
        "test_group": if_testgroup_selected
    }
    print(f"Request -> page: {page} | durations: {durations} | regions: {regions} | conditions: {conditions} | test_groups: {test_groups} | query: {others}\n\
Response -> Total test num: {total_data_num} | Total Page num: {total_page}")
    return jsonify(res)



#########################################################################################################
##### Individual ECGTest View
# Return Individual ECG Test Info & TestGroup List
#########################################################################################################
@ecgtest.route('/ecgtest/<int:id_>', methods=['GET'])
def get_ecgtest_info(id_):
    # Get Query
    get_ecgtest_query = query.q_get_ecgtest_info(id=id_)
    get_testgroup_query = query.q_get_ecgtest_testgroup(id=id_)
    # Get ECGTest
    # print(f"SQL QUERY IS : {get_ecgtest_query}")
    cur = db.cursor()
    cur.execute(get_ecgtest_query)
    ecg_test = [dict(row) for row in cur.fetchall()][0]
    cur.close()
    db.commit()
    # GET TestGroup
    # print(f"SQL QUERY IS : {get_testgroup_query}")
    cur = db.cursor()
    cur.execute(get_testgroup_query)
    test_groups = [dict(row) for row in cur.fetchall()]
    cur.close()
    db.commit()
    # Get Details
    details_path = os.path.join(current_app.config['DATA_ROOT_DIR'], ecg_test['details_path'][7:])
    hr, start_time, actual_duration = get_details(details_path)
    # Get Signal
    edf_path = os.path.join(current_app.config['DATA_ROOT_DIR'], ecg_test['edf_path'][7:])
    signal = get_ecg_data(edf_path)
    total_page = math.ceil(len(signal)/float(len_per_page))


    res = {
        "details": {
            "hr": hr,
            "start_time": start_time,
            "actual_duration": actual_duration,
            "file_path": edf_path
        },
        "test_group": test_groups,
        "id": ecg_test["id"],
        "region": ecg_test["region"],
        "seq": ecg_test["seq"],
        "duration": ecg_test["duration"],
        "condition": ecg_test["condition"],
        "total_page": total_page
    }
    print(f"Request -> EcgTest ID: {id_}\nResponse -> TestGroup Num: {len(test_groups)} | EcgSignal Total Len: {len(signal)} | TotalPage Num: {total_page}")
    return jsonify(res)



#########################################################################################################
##### Get ECG Image Path & SampleGroup Info
# Return ecg image png file path & sample group info list
#########################################################################################################
@ecgtest.route('/ecgtest/<int:id_>/<int:page>', methods=['GET'])
def make_ecg_png(id_, page):
    image_path_dump = []
    pid = request.args.get('pid', 0, type=int)


    # File 존재 유무 check
    exist_result = file_exist_check(id=id_, page=page)
    if exist_result is None:   # 없을 시
        # Get ecgtest info & ecg data
        get_ecgtest_query = query.q_get_ecgtest_info(id=id_)
        # print(f"SQL QUERY IS : {get_ecgtest_query}")
        cur = db.cursor()
        cur.execute(get_ecgtest_query)
        ecg_test = [dict(row) for row in cur.fetchall()][0]
        cur.close()

        # Strip Signal
        edf_path = os.path.join(current_app.config['DATA_ROOT_DIR'], ecg_test['edf_path'][7:])
        strip_signal = get_ecg_data(edf_path, (page-1)*len_per_page, len_per_page)

        # Save to PNG File & Get File Path
        file_name = signal_plot_to_png(signal=strip_signal, id=id_, page=page, one_image_len=one_image_len)
        image_file = url_for('static', filename='ecg_png_cache/' + file_name)
        image_path_dump.append(image_file)

    else:   # 있을 시
        image_file = url_for('static', filename='ecg_png_cache/' + exist_result)
        image_path_dump.append(image_file)

    # Pre-processing이 있을 시
    if pid != 0:
        prepro_suff = f"_preprocessed_{pid}"
        exist_result = file_exist_check(id=id_, page=page, add_name=prepro_suff)
        if exist_result is None:
            # Get Pre-processing method
            get_preprocess_query = query.q_get_preprocess_path(pid=pid)
            # print(f"SQL QUERY IS : {get_preprocess_query}")
            cur = db.cursor()
            cur.execute(get_preprocess_query)
            pre_process_file = [dict(row) for row in cur.fetchall()]
            cur.close()

            if len(pre_process_file) == 1:
                # Get ecgtest info & ecg data
                get_ecgtest_query = query.q_get_ecgtest_info(id=id_)
                # print(f"SQL QUERY IS : {get_ecgtest_query}")
                cur = db.cursor()
                cur.execute(get_ecgtest_query)
                ecg_test = [dict(row) for row in cur.fetchall()][0]
                cur.close()
                # Get Signal
                edf_path = os.path.join(current_app.config['DATA_ROOT_DIR'], ecg_test['edf_path'][7:])
                signal = get_ecg_data(edf_path)
                pre_process_file_path = pre_process_file[0]["path"]
                pre_method = process_module[pre_process_file_path]
                # Pre-processing
                processed_signal = pre_method(signal)
                strip_processed_signal = processed_signal[(page-1)*len_per_page:page*len_per_page]
                # Save to PNG File & Get File Path
                processed_file_name = signal_plot_to_png(signal=strip_processed_signal, id=id_, page=page, one_image_len=one_image_len, add_name=prepro_suff)
                processed_image_file = url_for('static', filename='ecg_png_cache/' + processed_file_name)
                image_path_dump.append(processed_image_file)
            else:
                print("There Is No Preprocessing File ID")

        else:
            processed_image_file = url_for('static', filename='ecg_png_cache/' + exist_result)
            image_path_dump.append(processed_image_file)
            
    # Get Sample Group Info
    cur = db.cursor()
    get_samplegroup_query = query.q_get_ecgtest_samplegroup(id=id_, page=page)
    cur.execute(get_samplegroup_query)
    sample_groups = [dict(row) for row in cur.fetchall()]
    cur.close()


    res = {
        "image_path": image_path_dump,
        "sample_group": sample_groups
    }
    print(f"Request -> ID: {id_} | Page: {page} | PID: {pid}\n\
Respoonse -> ImagePath: {image_path_dump} | SampleGroup Num: {len(sample_groups)}")
    return jsonify(res)










    


