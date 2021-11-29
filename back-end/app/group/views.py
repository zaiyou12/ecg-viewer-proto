from flask import jsonify, request

from app import db
from . import group
from . import query


#########################################################################################################
##### Get Group List
# Return group list info
#########################################################################################################
@group.route('/group/<string:type_>/list', methods=['GET'])
def get_group_list(type_):
    get_grouplist_query = query.q_get_grouplist(type_=type_)
    # print(f"SQL QUERY IS : {get_grouplist_query}")
    cur = db.cursor()
    cur.execute(get_grouplist_query)
    group_list = [dict(row) for row in cur.fetchall()]
    cur.close()

    new_group_list = []
    for group in group_list:
        if type_ == "p":
            group["num_tests"] = 0
            group["group_status"] = "open"
            new_group_list.append(group)
        else:
            group_id = group["id"]
            get_num_from_link_query = query.q_get_num_from_link(type_=type_, group_id=group_id)
            cur = db.cursor()
            cur.execute(get_num_from_link_query)
            num_tests = [dict(row) for row in cur.fetchall()][0]["COUNT(ecgtest_id)"]
            cur.close()

            group["num_tests"] = num_tests
            new_group_list.append(group)

    res = {
        "total_num": len(new_group_list),
        "type": type_,
        "group_list": new_group_list
    }
    print(f"Request -> Type: {type_}\nResponse -> Total Group Num: {len(new_group_list)}")
    return jsonify(res)




#########################################################################################################
##### Get ecgtest List From Group
#########################################################################################################
@group.route('/group/<string:type_>/<int:id_>', methods=['GET'])
def get_ecgtest_from_group(type_, id_):
    if type_ == "t":
        get_ecgtest_query = query.q_get_ecginfo_from_link(type_=type_, group_id=id_)
        # print(f"SQL QUERY IS : {get_ecgtest_query}")
        cur = db.cursor()
        cur.execute(get_ecgtest_query)
        ecgtest_list = [dict(row) for row in cur.fetchall()]

        new_ecgtest_list = []
        for ecg in ecgtest_list:
            ecg["pages"] = []
            new_ecgtest_list.append(ecg)
        
        cur.close()

    
    elif type_ == "s":
        get_ecgtest_query = query.q_get_ecginfo_from_link(type_=type_, group_id=id_)
        # print(f"SQL QUERY IS : {get_ecgtest_query}")
        cur = db.cursor()
        cur.execute(get_ecgtest_query)
        ecgtest_list = [dict(row) for row in cur.fetchall()]

        new_ecgtest_list = []
        for ecg in ecgtest_list:
            get_pageinfo_query = query.q_get_page_info(ecgtest_id=ecg["id"], group_id=id_)
            cur.execute(get_pageinfo_query)
            pageinfo_list = [dict(row) for row in cur.fetchall()]
            new_page_list = []
            for pageinfo in pageinfo_list:
                new_page_list.append(pageinfo["page"])
            ecg["pages"] = new_page_list
            new_ecgtest_list.append(ecg)

        cur.close()

    res = {
        "type": type_,
        "tests": new_ecgtest_list
    }
    print(f"Request -> Type: {type_} | ID: {id_}\nResponse -> Total ECGTest Num: {len(new_ecgtest_list)}")
    return jsonify(res)



#########################################################################################################
##### Post group add
#########################################################################################################
@group.route('/group/<string:type_>/add', methods=['POST'])
def create_group(type_):
    group_name = request.json.get("group_name")
    # Check exist
    get_group_data_query = query.q_get_groupdata_from_name(type_=type_, group_name=group_name)
    # print(f"SQL QUERY IS : {get_group_data_query}")
    cur = db.cursor()
    cur.execute(get_group_data_query)
    groups = [dict(row) for row in cur.fetchall()]
    cur.close()
    if len(groups)==1:
        res = {
            "message": "Already Added",
            "id": groups[0]['id']
        }
        print(f"Request -> Type: {type_} | Group Name: {group_name}\nResponse -> Message: 'Already Added' | ID: {groups[0]['id']}")
        return jsonify(res)


    if type_ == "t" or type_ == "s":
        group_status = request.json.get("group_status")

        create_group_query = query.q_create_groupdata(type_=type_, group_name=group_name, group_status=group_status)
        # print(f"SQL QUERY IS : {create_group_query}")
        cur = db.cursor()
        cur.execute(create_group_query)
        db.commit()

        # Get group id
        get_group_data_query = query.q_get_groupdata_from_name(type_=type_, group_name=group_name)
        cur.execute(get_group_data_query)
        groups = [dict(row) for row in cur.fetchall()]
        res = {
            "message": "Added",
            "id": groups[0]['id']
        }

    elif type_ == "p":
        path = request.json.get("path")

        create_group_query = query.q_create_groupdata(type_=type_, group_name=group_name, path=path)
        # print(f"SQL QUERY IS : {create_group_query}")
        cur = db.cursor()
        cur.execute(create_group_query)
        db.commit()

        # Get group id
        get_group_data_query = query.q_get_groupdata_from_name(type_=type_, group_name=group_name)
        cur.execute(get_group_data_query)
        groups = [dict(row) for row in cur.fetchall()]
        res = {
            "message": "Added",
            "id": groups[0]['id']
        }

    cur.close()
    print(f"Request -> Type: {type_} | Group Name: {group_name}\nResponse -> Message: 'Added' | ID: {groups[0]['id']}")
    return jsonify(res)




#########################################################################################################
##### Post group delete
#########################################################################################################
@group.route('/group/<string:type_>/del', methods=['POST'])
def delete_group(type_):
    group_id = request.json.get("id")

    get_group_data_query = query.q_get_groupdata_from_id(type_=type_, id_=group_id)
    # print(f"SQL QUERY IS : {get_group_data_query}")
    cur = db.cursor()
    cur.execute(get_group_data_query)
    groups = [dict(row) for row in cur.fetchall()]

    if len(groups)==1:
        delete_query = query.q_delete_groupdata(type_=type_, id_=group_id)
        cur.execute(delete_query)
        db.commit()
        res = {
            "message": "Deleted",
            "id": group_id
        }
        print(f"Request -> Type: {type_} | Group ID: {group_id}\nResponse -> Message: 'Deleted' | ID: {group_id}")
        cur.close()
        return jsonify(res)

    else:
        res = {
            "message": "Already Deleted",
            "id": group_id
        }
        print(f"Request -> Type: {type_} | Group ID: {group_id}\nResponse -> Message: 'Already Deleted' | ID: {group_id}")
        cur.close()
        return jsonify(res)



#########################################################################################################
##### Post group change
#########################################################################################################
@group.route('/group/<string:type_>/change', methods=['POST'])
def change_group(type_):
    works = request.json.get("works")
    group_id = request.json.get("id")
    act = request.json.get("act")

    cur = db.cursor()
    results = []
    if act == "add":   # 추가
        for work in works:
            result = {}
            check_link_query = query.q_get_link(type_=type_, group_id=group_id, work=work)
            cur.execute(check_link_query)
            links = [dict(row) for row in cur.fetchall()]
            if len(links) == 0:   # link가 없는 경우 -> "Added"
                create_link_query = query.q_create_link(type_=type_, group_id=group_id, work=work)
                cur.execute(create_link_query)
                db.commit()
                
                result["target"] = work
                result["message"] = "Added"
            else:   # link가 있는 경우 -> "Already Added"
                result["target"] = work
                result["message"] = "Already Added"

            results.append(result)

    else:   # 제거
        for work in works:
            result = {}
            check_link_query = query.q_get_link(type_=type_, group_id=group_id, work=work)
            cur.execute(check_link_query)
            links = [dict(row) for row in cur.fetchall()]
            if len(links) == 1:   # link가 있는 경우 "Deleted"
                delete_link_query = query.q_delete_link(type_=type_, group_id=group_id, work=work)
                cur.execute(delete_link_query)
                db.commit()

                result["target"] = work
                result["message"] = "Deleted"
            else:   # link가 없는 경우 "Already Deleted"
                result["target"] = work
                result["message"] = "Already Deleted"

            results.append(result)

    cur.close()

    res = {
        "id": group_id,
        "result": results
    }
    print(f"Request -> Type: {type_} | Group ID: {group_id} | Act: {act}\nResponse -> Do Num: {len(results)}")
    return jsonify(res)















