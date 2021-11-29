import sqlite3

import os
import sys

# 초기 경로
base_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
db_path = os.path.join(base_dir, "sqlite.db")


########################################################################################### 테이블 생성
def create_table(con):
    cur = con.cursor()
    # ecgtest Table 생성
    query = """\
CREATE TABLE ecgtest
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    seq TEXT NOT NULL,
    region TEXT NOT NULL,
    duration TEXT NOT NULL,
    condition TEXT DEFAULT 'unknown',
    edf_path TEXT NOT NULL,
    details_path TEXT DEFAULT './'
)"""
    cur.execute(query)
    # tesgroup Table 생성
    query = """\
CREATE TABLE testgroup
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    group_name TEXT UNIQUE NOT NULL,
    group_status TEXT DEFAULT 'open'
)"""
    cur.execute(query)
    # samplegroup Table 생성
    query = """\
CREATE TABLE samplegroup
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    group_name TEXT UNIQUE NOT NULL,
    group_status TEXT DEFAULT 'open'
)"""
    cur.execute(query)
    # preprocessgroup Table 생성
    query = """\
CREATE TABLE preprocessgroup
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    group_name TEXT UNIQUE NOT NULL,
    path TEXT NOT NULL
)"""
    cur.execute(query)
    # testlink Table 생성
    query = """\
CREATE TABLE testlink
(
    ecgtest_id INTEGER,
    testgroup_id INTEGER,
    FOREIGN KEY(ecgtest_id) REFERENCES ecgtest(id),
    FOREIGN KEY(testgroup_id) REFERENCES testgroup(id),
    PRIMARY KEY(ecgtest_id, testgroup_id)
)"""
    cur.execute(query)
    # samplelink Table 생성
    query = """\
CREATE TABLE samplelink
(
    ecgtest_id INTEGER,
    samplegroup_id INTEGER,
    page NOT NULL,
    FOREIGN KEY(ecgtest_id) REFERENCES ecgtest(id),
    FOREIGN KEY(samplegroup_id) REFERENCES samplegroup(id),
    PRIMARY KEY(ecgtest_id, samplegroup_id, page)
)"""
    cur.execute(query)
    cur.close()
    con.commit()


########################################################################################### ECGTest Data Input
def ecgtest_data_input(con):
    cur = con.cursor()

    edf_file_list_path = "/home/wellysis-tft/Desktop/pipeline/au-db/AU"
    end_ = ""
    for (root, directs, files) in os.walk(edf_file_list_path):
        for file_ in files:
            file_path = os.path.join(root, file_)

            seq = root.split("_")[-1].strip()
            dur = root.split("/")[-2].strip()
            if end_ != seq:
                query = f"INSERT INTO ecgtest (seq, region, duration, edf_path) VALUES ('{seq}', 'AU', '{dur}', '{file_path}')"
                cur.execute(query)
                end_ = seq

    cur.close()
    con.commit()


########################################################################################### Samplegroup Data Input
def samplegroup_data_input(con, save_num=30):
    cur = con.cursor()
    for idx in range(save_num):
        query = f"INSERT INTO samplegroup (group_name) VALUES ('a01_samplegroup_{idx}')"
        cur.execute(query)
    cur.close()
    con.commit()


########################################################################################### Testgroup Data Input
def testgroup_data_input(con, save_num=30):
    cur = con.cursor()
    for idx in range(save_num):
        query = f"INSERT INTO testgroup (group_name) VALUES ('a01_testgroup_{idx}')"
        cur.execute(query)
    cur.close()
    con.commit()



########################################################################################### Preprocess Data Input
def preprocessgroup_data_input(con):
    cur = con.cursor()
    query = f"INSERT INTO preprocessgroup (group_name, path) VALUES ('bandwith_process', 'bandwith_process')"
    cur.execute(query)
    cur.close()
    con.commit()


if __name__ == "__main__":
    # DB 연결
    con = sqlite3.connect(db_path)
    create_table(con)

    ecgtest_data_input(con)
    samplegroup_data_input(con)
    testgroup_data_input(con)
    preprocessgroup_data_input(con)
    con.close()

