

##### ----- 개별 ECG Test의 정보
def q_get_ecgtest_info(region: str, test_id: str) -> str:
    query = f"SELECT id, region, test_id, duration, condition, edf_path, details_path \
FROM ecgtest \
WHERE region='{region}' AND test_id='{test_id}'"
    return query



##### ----- Make Link ECGTest-TestGroup
def q_make_link_ecgtest_testgroup(ecgtest_id: int, testgroup_id: int) -> str:
    query = f"INSERT INTO testlink (ecgtest_id, testgroup_id) VALUES ({ecgtest_id}, {testgroup_id})"
    return query



##### ----- Delete Link ECGTest-TestGroup
def q_delete_link_ecgtest_testgroup(ecgtest_id: int, testgroup_id: int) -> str:
    query = f"DELETE FROM testlink WHERE ecgtest_id={ecgtest_id} AND testgroup_id={testgroup_id}"
    return query



##### ----- Get Link ECGTest-TestGroup
def q_get_testlink(ecgtest_id: int, testgroup_id: int) -> str:
    query = f"SELECT ecgtest_id, testgroup_id FROM testlink WHERE ecgtest_id={ecgtest_id} AND testgroup_id={testgroup_id}"
    return query



##### ----- Get Link ECGTest-SampleGroup
def q_get_samplelink(ecgtest_id: int, page: int, samplegroup_id: int) -> str:
    query = f"SELECT ecgtest_id, page, samplegroup_id FROM samplelink WHERE ecgtest_id={ecgtest_id} AND page={page} AND samplegroup_id={samplegroup_id}"
    return query



##### ----- Make Link ECGTest-SampleGroup
def q_make_link_ecgtest_samplegroup(ecgtest_id: int, page: int, samplegroup_id: int) -> str:
    query = f"INSERT INTO samplelink (ecgtest_id, samplegroup_id, page) VALUES ({ecgtest_id}, {samplegroup_id}, {page})"
    return query



##### ----- Delete Link ECGTest-SampleGroup
def q_delete_link_ecgtest_samplegroup(ecgtest_id: int, page: int, samplegroup_id: int) -> str:
    query = f"DELETE FROM samplelink WHERE ecgtest_id={ecgtest_id} AND samplegroup_id={samplegroup_id} AND page={page}"
    return query



##### ----- Delete Link ECGTest-SampleGroup
def q_get_grouplist(type_: str) -> str:
    table=None
    if type_ == "t":
        table="testgroup"
    elif type_ == "s":
        table="samplegroup"
    else:
        table="preprocessgroup"
    
    query = f"SELECT id, group_name FROM {table}"
    return query


##### ----- Insert Data to Group
def q_create_groupdata(ty: str, group_name: str, group_status: str, path: str) -> str:
    if ty == "t":
        query = f"INSERT INTO testgroup (group_name, group_status) VALUES ('{group_name}', '{group_status}')"
    elif ty == "s":
        query = f"INSERT INTO samplegroup (group_name, group_status) VALUES ('{group_name}', '{group_status}')"
    else:
        query = f"INSERT INTO preprocessgroup (group_name, group_status, path) VALUES ('{group_name}', '{group_status}', '{path}')"
    return query