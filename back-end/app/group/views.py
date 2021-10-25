from flask import jsonify, request

from app import db
from . import group
from . import query


#########################################################################################################
##### POST TestGroup Link
# Make ecgtest - testgroup link
#########################################################################################################
@group.route('/ecgtest/<string:region>/<string:test_id>', methods=['POST'])
def link_ecgtest_testgroup(region, test_id):
    test_group_id = request.json.get("test_group_id")
    status = request.json.get("status")
    message = None
    # Get ecgtest
    get_ecgtest_query = query.q_get_ecgtest_info(region=region, test_id=test_id)
    cur = db.cursor()
    cur.execute(get_ecgtest_query)
    ecg_test_id = [dict(row) for row in cur.fetchall()][0]["id"]
    cur.close()
    db.commit()
    print(f"SQL QUERY IS : {get_ecgtest_query}")
    # Check Data exist
    get_testlink_query = query.q_get_testlink(ecgtest_id=ecg_test_id, testgroup_id=test_group_id)
    cur = db.cursor()
    cur.execute(get_testlink_query)
    test_links = [dict(row) for row in cur.fetchall()]
    cur.close()
    db.commit()
    if status:   # If Status == True --> Adding
        if len(test_links)==0:
            make_link_query = query.q_make_link_ecgtest_testgroup(ecgtest_id=ecg_test_id, testgroup_id=test_group_id)
            cur = db.cursor()
            cur.execute(make_link_query)
            cur.close()
            db.commit()
            message = "Added"
            print(f"SQL QUERY IS : {make_link_query}")
        else:
            message = "Already exist"
    else:   # If Status == False --> Delete
        if len(test_links)==1:
            delete_link_query = query.q_delete_link_ecgtest_testgroup(ecgtest_id=ecg_test_id, testgroup_id=test_group_id)
            cur = db.cursor()
            cur.execute(delete_link_query)
            cur.close()
            db.commit()
            message = "Deleted"
            print(f"SQL QUERY IS : {delete_link_query}")
        else:
            message = "Already None"

    res = {
        "message": message,
        "test_id": test_id,
        "test_group_id": test_group_id
    }
    print(f"Request -> Region: {region} | Test ID: {test_id} | TestGroup ID: {test_group_id} | Status: {status}\n\
Response -> Message: '{message}' | ECGTest ID: {ecg_test_id} | TESTGroup ID: {test_group_id}")
    return jsonify(res)



#########################################################################################################
##### POST SampleGroup Link
# Make ecgtest - samplegroup link
#########################################################################################################
@group.route('/ecgtest/<string:region>/<string:test_id>/<int:page>', methods=['POST'])
def link_ecgtest_samplegroup(region, test_id, page):
    sample_group_id = request.json.get("sample_group_id")
    status = request.json.get("status")
    message = None
    # Get ecgtest
    get_ecgtest_query = query.q_get_ecgtest_info(region=region, test_id=test_id)
    cur = db.cursor()
    cur.execute(get_ecgtest_query)
    ecg_test_id = [dict(row) for row in cur.fetchall()][0]["id"]
    cur.close()
    db.commit()
    print(f"SQL QUERY IS : {get_ecgtest_query}")
    # Check Data exist
    get_samplelink_query = query.q_get_samplelink(ecgtest_id=ecg_test_id, page=page, samplegroup_id=sample_group_id)
    cur = db.cursor()
    cur.execute(get_samplelink_query)
    sample_links = [dict(row) for row in cur.fetchall()]
    cur.close()
    db.commit()
    if status:   # If Status == True --> Adding
        if len(sample_links)==0:
            make_link_query = query.q_make_link_ecgtest_samplegroup(ecgtest_id=ecg_test_id, samplegroup_id=sample_group_id, page=page)
            cur = db.cursor()
            cur.execute(make_link_query)
            cur.close()
            db.commit()
            message = "Added"
            print(f"SQL QUERY IS : {make_link_query}")
        else:
            message = "Already exist"
    else:   # If Status == False --> Delete
        if len(sample_links)==1:
            delete_link_query = query.q_delete_link_ecgtest_samplegroup(ecgtest_id=ecg_test_id, samplegroup_id=sample_group_id, page=page)
            cur = db.cursor()
            cur.execute(delete_link_query)
            cur.close()
            db.commit()
            message = "Deleted"
            print(f"SQL QUERY IS : {delete_link_query}")
        else:
            message = "Already None"

    res = {
        "message": message,
        "test_id": test_id,
        "page": page,
        "sample_group_id": sample_group_id
    }
    print(f"Request -> Region: {region} | Test ID: {test_id} | SampleGroup ID: {sample_group_id} | Page:{page} | Status: {status}\n\
Response -> Message: '{message}' | ECGTest ID: {ecg_test_id} | Page: {page} | SampleGroup ID: {sample_group_id}")
    return jsonify(res)



#########################################################################################################
##### Get Group List
# Return group list info
#########################################################################################################
@group.route('/group', methods=['GET'])
def get_group_list():
    type_ = request.args.get('type', type=str)   # "t" | "s" | "p"

    get_grouplist_query = query.q_get_grouplist(type_=type_)
    cur = db.cursor()
    cur.execute(get_grouplist_query)
    group_list = [dict(row) for row in cur.fetchall()]
    cur.close()
    db.commit()
    print(f"SQL QUERY IS : {get_grouplist_query}")
    res = {
        "total_num": len(group_list),
        "type": type_,
        "group_list": group_list
    }
    print(f"Request -> Type: {type_}\nResponse -> Total Group Num: {len(group_list)}")
    return jsonify(res)




#########################################################################################################
##### Create TestGroup
#########################################################################################################
@group.route('/group/<string:ty>', methods=['POST'])
def create_group(ty):
    group_name = request.json.get("group_name")
    group_status = request.json.get("group_status")
    path = request.json.get("path")

    create_groupdata_query = query.q_create_groupdata(ty=ty, group_name=group_name, group_status=group_status, path=path)
    cur = db.cursor()
    cur.execute(create_groupdata_query)
    cur.close()
    db.commit()
    print(f"SQL QUERY IS : {create_groupdata_query}")
    res = {
        "message": "Created",
        "type": ty,
        "group_name": group_name,
        "group_status": group_status,
        "path": path
    }
    print(f"Request -> Type: {ty} | Group Name: {group_name} | Group Status: {group_status} | Path: {path}\nResponse -> Message: Created")
    return jsonify(res)
