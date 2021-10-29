from typing import List

##### ----- Format을 위한
def make_tuple_from_list(list_data: list) -> str:
    text ="("
    idx = 0
    for data in list_data:
        if isinstance(data, str):
            data = f"'{data}'"
        else:
            data = str(data)
        if idx != 0 :
            text +=  f", {data}"
            idx+=1
        else:
            text += data
            idx+=1
    return text + ")"

def make_tuple_from_string(text_list: List[str]) -> str:
    idx = 0
    qu = "(SELECT * FROM ecgtest WHERE "
    for text in text_list:
        if idx != 0:
            qu += f" OR test_id LIKE '%{text}%'"
        else:    
            qu += f"test_id LIKE '%{text}%'"
            idx+=1
    qu += ")"
    return qu
    

##### ----- ECG Test List 반환
def q_get_ecgtests(durations: List[str], regions: List[str], conditions: List[str], test_groups: List[str], others: List[str]) -> str:
    base_table = None
    if others:
        text_list = others.replace(",","").split(" ")
        base_table = make_tuple_from_string(text_list=text_list)
    else:
        base_table = "ecgtest"

    query = f"SELECT region, test_id, duration, condition FROM {base_table} "
    # Apply Condition
    if len(durations+regions+conditions+test_groups) >= 1:
        query += "WHERE "

        where_qu = ""
        if len(durations)>=1:
            where_qu += f"AND duration IN {make_tuple_from_list(durations)} "
        if len(regions)>=1:
            where_qu += f"AND region IN {make_tuple_from_list(regions)} "
        if len(conditions)>=1:
            where_qu += f"AND condition IN {make_tuple_from_list(conditions)} "
        if len(test_groups)>=1:
            where_qu += f"AND id IN (SELECT ecgtest_id FROM testlink WHERE testgroup_id IN {make_tuple_from_list(test_groups)}) "

        query += where_qu[4:]

    query += f"ORDER BY test_id"
    return query



##### ----- 개별 ECG Test의 정보
def q_get_ecgtest_info(region: str, test_id: str) -> str:
    query = f"SELECT region, test_id, duration, condition, edf_path, details_path \
FROM ecgtest \
WHERE region='{region}' AND test_id='{test_id}'"
    return query



##### ----- 개별 ECG Test가 속해져 있는 TestGroup ID 가져오기
def q_get_ecgtest_testgroup(region: str, test_id: str) -> str:
    query = f"SELECT id, group_name FROM testgroup WHERE id IN (\
SELECT testgroup_id FROM testlink WHERE ecgtest_id IN (\
SELECT id FROM ecgtest WHERE region='{region}' AND test_id='{test_id}'))"
    return query



##### ----- Preprocess file path 가져오기
def q_get_preprocess_path(pid: int) -> str:
    query = f"SELECT id, group_name, group_status, path FROM preprocessgroup WHERE id={pid}"
    return query



##### ----- 개별 ECG Test&Page가 속해져 있는 SampleGroup ID 가져오기
def q_get_ecgtest_samplegroup(region: str, test_id: str, page: int) -> str:
    query = f"SELECT id, group_name FROM samplegroup WHERE id IN (\
SELECT samplegroup_id FROM samplelink WHERE page={page} AND ecgtest_id IN(\
SELECT id FROM ecgtest WHERE region='{region}' AND test_id='{test_id}'))"
    return query



