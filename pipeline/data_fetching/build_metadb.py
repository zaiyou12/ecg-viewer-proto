import sqlite3

import os
import sys
from config import Config

db_path = Config.recording_db_path

########################################################################################### 테이블 생성
def create_table(con):
    cur = con.cursor()
    # ecgtest Table 생성
    query = """\
CREATE TABLE ecgtest
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    seq TEXT NOT NULL,
    org_id INTEGER NOT NULL,
    site_id INTEGER NOT NULL,
    region TEXT NOT NULL,
    duration TEXT NOT NULL,
    condition TEXT DEFAULT 'unknown',
    edf_path TEXT NOT NULL,
    details_path TEXT DEFAULT './',
    for_unique TEXT NOT NULL UNIQUE,
    FOREIGN KEY(org_id) REFERENCES org(org_id),
    FOREIGN KEY(site_id) REFERENCES site(site_id)
)"""
    cur.execute(query)
    print("ecgtest Table created!")

    # tesgroup Table 생성
    query = """\
CREATE TABLE testgroup
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    group_name TEXT UNIQUE NOT NULL,
    group_status TEXT DEFAULT 'open'
)"""
    cur.execute(query)
    print("testgroup Table created!")

    # samplegroup Table 생성
    query = """\
CREATE TABLE samplegroup
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    group_name TEXT UNIQUE NOT NULL,
    group_status TEXT DEFAULT 'open'
)"""
    cur.execute(query)
    print("samplegroup Table created!")

    # preprocessgroup Table 생성
    query = """\
CREATE TABLE preprocessgroup
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    group_name TEXT UNIQUE NOT NULL,
    path TEXT NOT NULL
)"""
    cur.execute(query)
    print("preprocessgroup Table created!")

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
    print("testlink Table created!")

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
    print("samplelink Table created!")

    # org Table 생성
    query = """\
CREATE TABLE org
(
    org_id INTEGER NOT NULL,
    org_code TEXT,
    org_name TEXT,
    PRIMARY KEY(org_id)
)"""
    cur.execute(query)
    print("org Table created!")

    # site Table 생성
    query = """\
CREATE TABLE site
(
    site_id INTEGER NOT NULL,
    site_code TEXT,
    site_name TEXT,
    PRIMARY KEY(site_id)
)"""
    cur.execute(query)
    print("site Table created!")

    cur.close()
    con.commit()


if __name__ == "__main__":
    # DB 연결
    print(db_path)
    con = sqlite3.connect(db_path)
    create_table(con)
    con.close()
