from typing import Union


##### ----- Delete Link ECGTest-SampleGroup
def q_get_grouplist(type_: str) -> str:
    table=None
    if type_ == "t":
        query = "SELECT id, group_name, group_status FROM testgroup"
        return query
    elif type_ == "s":
        query = "SELECT id, group_name, group_status FROM samplegroup"
        return query
    elif type_ == "p":
        query = "SELECT id, group_name FROM preprocessgroup"
        return query
    return -1


##### ----- Insert Data to Group
def q_create_groupdata(type_: str, group_name: str, group_status: str = "Open", path:str = "./") -> str:
    if type_ == "t":
        query = f"INSERT INTO testgroup (group_name, group_status) VALUES ('{group_name}', '{group_status}')"
    elif type_ == "s":
        query = f"INSERT INTO samplegroup (group_name, group_status) VALUES ('{group_name}', '{group_status}')"
    else:
        query = f"INSERT INTO preprocessgroup (group_name, path) VALUES ('{group_name}', '{path}')"
    return query



##### ----- Get Count from Link db
def q_get_num_from_link(type_: str, group_id: int) -> str:
    if type_ == "t":
        query = f"SELECT COUNT(ecgtest_id) FROM testlink WHERE testgroup_id={group_id}"
        return query
    elif type_ == "s":
        query = f"SELECT COUNT(ecgtest_id) FROM samplelink WHERE samplegroup_id={group_id}"
        return query
    return -1



##### ----- Get ecg info from link
def q_get_ecginfo_from_link(type_: str, group_id: int) -> str:
    base_query = "SELECT T.id AS id, T.region AS region, O.org_code AS org_code, S.site_name AS site_name, T.seq AS seq, T.duration AS duration, T.condition AS condition \
FROM ecgtest AS T JOIN org AS O ON T.org_id = O.org_id JOIN site AS S ON T.site_id = S.site_id \
WHERE T.id IN"

    if type_ == "t":
        query = f"{base_query} (SELECT ecgtest_id FROM testlink WHERE testgroup_id={group_id})"
        return query

    elif type_ == "s":
        query = f"{base_query} (SELECT ecgtest_id FROM samplelink WHERE samplegroup_id={group_id})"
        return query
    
    return -1



##### ----- Get page info from link
def q_get_page_info(ecgtest_id: int, group_id: int) -> str:
    query = f"SELECT page FROM samplelink WHERE ecgtest_id={ecgtest_id} AND samplegroup_id={group_id}"
    return query



##### ----- Get group data From name
def q_get_groupdata_from_name(type_: str, group_name: str) -> str:
    if type_ == "t":
        query = f"SELECT id, group_name FROM testgroup WHERE group_name='{group_name}'"
        return query
    if type_ == "s":
        query = f"SELECT id, group_name FROM samplegroup WHERE group_name='{group_name}'"
        return query
    if type_ == "p":
        query = f"SELECT id, group_name FROM preprocessgroup WHERE group_name='{group_name}'"
        return query
    return -1



##### ----- Get group data From ID
def q_get_groupdata_from_id(type_: str, id_: int) -> str:
    if type_ == "t":
        query = f"SELECT id, group_name FROM testgroup WHERE id={id_}"
        return query
    if type_ == "s":
        query = f"SELECT id, group_name FROM samplegroup WHERE id={id_}"
        return query
    if type_ == "p":
        query = f"SELECT id, group_name FROM preprocessgroup WHERE id={id_}"
        return query
    return -1



##### ----- Delete group data
def q_delete_groupdata(type_: str, id_: int) -> str:
    if type_ == "t":
        query = f"DELETE FROM testgroup WHERE id={id_}"
        return query
    if type_ == "s":
        query = f"DELETE FROM samplegroup WHERE id={id_}"
        return query
    if type_ == "p":
        query = f"DELETE FROM preprocessgroup WHERE id={id_}"
        return query
    return -1



##### ----- Make Link
def q_create_link(type_: str, group_id: int, work: Union[list, int]) -> str:
    if type_ == "t":
        query = f"INSERT INTO testlink (ecgtest_id, testgroup_id) VALUES ({work}, {group_id})"
        return query
    elif type_ == "s":
        query = f"INSERT INTO samplelink (ecgtest_id, samplegroup_id, page) VALUES ({work[0]}, {group_id}, {work[1]})"
        return query
    return -1



##### ----- Get Link
def q_get_link(type_: str, group_id: int, work: Union[list, int]) -> str:
    if type_ == "t":
        query = f"SELECT ecgtest_id, testgroup_id FROM testlink WHERE ecgtest_id={work} AND testgroup_id={group_id}"
        return query
    elif type_ == "s":
        query = f"SELECT ecgtest_id, samplegroup_id, page FROM samplelink WHERE ecgtest_id={work[0]} AND samplegroup_id={group_id} AND page={work[1]}"
        return query
    return -1



##### ----- Delete Link
def q_delete_link(type_: str, group_id: int, work: Union[list, int]) -> str:
    if type_ == "t":
        query = f"DELETE FROM testlink WHERE ecgtest_id={work} AND testgroup_id={group_id}"
        return query
    elif type_ == "s":
        query = f"DELETE FROM samplelink WHERE ecgtest_id={work[0]} AND samplegroup_id={group_id} AND page={work[1]}"
        return query
    return -1