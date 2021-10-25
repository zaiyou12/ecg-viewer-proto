from flask import jsonify, send_file, request, url_for
import math

from . import ecgtest
from app import db

from .utils import get_details, ploting_from_signal, get_ecg_data, make_test_list_for_ecgtest, signal_plot_to_png, make_group_list_for_ecgtest
from . import query
from preprocess.pre_class import process_module


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
    print(f"SQL QUERY IS : {qu}")
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
@ecgtest.route('/ecgtest/<string:region>/<string:test_id>', methods=['GET'])
def get_ecgtest_info(region, test_id):
    # Get Query
    get_ecgtest_query = query.q_get_ecgtest_info(region=region, test_id=test_id)
    get_testgroup_query = query.q_get_ecgtest_testgroup(region=region, test_id=test_id)
    # Get ECGTest
    print(f"SQL QUERY IS : {get_ecgtest_query}")
    cur = db.cursor()
    cur.execute(get_ecgtest_query)
    ecg_test = [dict(row) for row in cur.fetchall()][0]
    cur.close()
    db.commit()
    # GET TestGroup
    print(f"SQL QUERY IS : {get_testgroup_query}")
    cur = db.cursor()
    cur.execute(get_testgroup_query)
    test_groups = [dict(row) for row in cur.fetchall()]
    cur.close()
    db.commit()

    # Get Details
    hr, start_time, actual_duration = get_details(ecg_test['details_path'])
    
    # Get Signal
    signal = get_ecg_data(ecg_test['edf_path'])
    len_per_page = 256 * 60 * 6   # hz x 1min x 6images   # Float
    total_page = math.ceil(len(signal)/float(len_per_page))

    res = {
        "details": {
            "hr": hr,
            "start_time": start_time,
            "actual_duration": actual_duration
        },
        "test_group": test_groups,
        "region": ecg_test["region"],
        "test_id": ecg_test["test_id"],
        "duration": ecg_test["duration"],
        "condition": ecg_test["condition"],
        "total_page": total_page
    }
    print(f"Request -> EcgTest Region: {region} | Test_ID: {test_id}\nResponse -> TestGroup Num: {len(test_groups)} | EcgSignal Total Len: {len(signal)} | TotalPage Num: {total_page}")
    return jsonify(res)



#########################################################################################################
##### Get ECG Image Path & SampleGroup Info
# Return ecg image png file path & sample group info list
#########################################################################################################
@ecgtest.route('/ecgtest/<string:region>/<string:test_id>/<int:page>', methods=['GET'])
def make_ecg_png(region, test_id, page):
    image_path_dump = []

    pid = request.args.get('pid', 0, type=int)
    # Get ecgtest info & ecg data
    get_ecgtest_query = query.q_get_ecgtest_info(region=region, test_id=test_id)
    cur = db.cursor()
    cur.execute(get_ecgtest_query)
    ecg_test = [dict(row) for row in cur.fetchall()][0]
    cur.close()
    db.commit()
    signal = get_ecg_data(ecg_test["edf_path"])
    print(f"SQL QUERY IS : {get_ecgtest_query}")
    # Strip Signal
    one_image_len = 256 * 60   # hz x 1min
    len_per_page = one_image_len * 6   # one_image_len x 6images
    total_page = math.ceil(len(signal)/float(len_per_page))
    strip_signal = signal[(page-1)*len_per_page:page*len_per_page]

    # Save to PNG File & Get File Path
    file_name = signal_plot_to_png(signal=strip_signal, region=region, test_id=test_id, page=page, one_image_len=one_image_len)
    image_file = url_for('static', filename='ecg_png_cache/' + file_name)
    image_path_dump.append(image_file)

    # Get Pre-processed file
    if pid != 0:
        # Get Pre-processing method
        get_preprocess_query = query.q_get_preprocess_path(pid=pid)
        cur = db.cursor()
        cur.execute(get_preprocess_query)
        pre_process_file = [dict(row) for row in cur.fetchall()]
        cur.close()
        db.commit()
        if len(pre_process_file)==1:
            pre_process_file_path = pre_process_file[0]["path"]
            pre_method = process_module[pre_process_file_path]
            # Pre-processing
            processed_signal = pre_method(signal)
            strip_processed_signal = processed_signal[(page-1)*len_per_page:page*len_per_page]
            # Save to PNG File & Get File Path
            processed_file_name = signal_plot_to_png(signal=strip_processed_signal, region=region, test_id=test_id, page=page, one_image_len=one_image_len, add_name="_preprocessed")
            processed_image_file = url_for('static', filename='ecg_png_cache/' + file_name)
            image_path_dump.append(processed_image_file)
            print(f"SQL QUERY IS : {get_preprocess_query}")
        else:
            print("There Is No Preprocessing File ID")
    # Get SampleGroup list
    get_samplegroup_query = query.q_get_ecgtest_samplegroup(region=region, test_id=test_id, page=page)
    cur = db.cursor()
    cur.execute(get_samplegroup_query)
    sample_groups = [dict(row) for row in cur.fetchall()]
    cur.close()
    db.commit()
    print(f"SQL QUERY IS : {get_samplegroup_query}")
    res = {
        "image_path": image_path_dump,
        "sample_group": sample_groups
    }
    print(f"Request -> Region: {region} | Test ID: {test_id} | Page: {page} | PID: {pid}\n\
Respoonse -> ImagePath: {image_path_dump} | SampleGroup Num: {len(sample_groups)} | Total Signal Len : {len(signal)}")
    return jsonify(res)



