
def q_get_test_all():
    query = f"""
SELECT id AS test_id, test_seq, recording_start_time,
TIMESTAMPDIFF(HOUR, recording_start_time, recording_end_time) AS duration,
org_id, site_id
FROM ecg_test;
"""
    return query


def q_get_test_with_constraint(org_id, site_id, test_sec):
    constraint = "WHERE "
    if org_id is not None:
        constraint += f"org_id={org_id} AND "
    if site_id is not None:
        constraint += f"site_id={site_id} AND "
    if test_sec is not None:
        constraint += f"test_sec={test_sec} AND "
    query = f"""
SELECT id AS test_id, test_seq, recording_start_time,
TIMESTAMPDIFF(HOUR, recording_start_time, recording_end_time) AS duration,
org_id, site_id
FROM ecg_test;
"""
    return query



def q_get_test_from_org_site(org_code, site_name):
    query = f"""
SELECT T.id AS test_id, test_seq, recording_start_time,
	TIMESTAMPDIFF(HOUR, T.recording_start_time, T.recording_end_time) as duration,
    org_id, site_id
FROM ecg_test AS T WHERE org_id IN (
    SELECT id FROM org WHERE org_code='{org_code}'
) AND site_id IN (
    SELECT site_id FROM site WHERE site_name='{site_name}'
);
"""
    return query


def q_get_blob_data(test_id):
    query = f"SELECT id, uploaded_file FROM ecg_test_uploading_files WHERE test_id = {test_id};"
    return query


def q_insert_metadata(seq, org_id, site_id, region, duration, edf_path, details_path, for_unique):
    query = f"INSERT INTO ecgtest (seq, org_id, site_id, region, duration, edf_path, details_path, for_unique) VALUES ('{seq}', {org_id}, {site_id}, '{region}', '{duration}', '{edf_path}', '{details_path}', '{for_unique}')"
    return query


def q_get_org_info():
    query = "SELECT id, org_code, org_name FROM org"
    return query


def q_get_site_info():
    query = "SELECT site_id, site_code, site_name FROM site"
    return query


def q_check_in_org(org_id):
    query = f"SELECT org_id FROM org WHERE org_id={org_id}"
    return query


def q_insert_to_org(org_id, org_code, org_name):
    org_name = org_name.replace("'", "''")
    query = f"INSERT INTO org (org_id, org_code, org_name) VALUES ({org_id}, '{org_code}', '{org_name}')"
    return query


def q_check_in_site(site_id):
    query = f"SELECT site_id FROM site WHERE site_id={site_id}"
    return query


def q_insert_to_site(site_id, site_code, site_name):
    site_name = site_name.replace("'", "''")
    query = f"INSERT INTO site (site_id, site_code, site_name) VALUES ({site_id}, '{site_code}', '{site_name}')"
    return query


def q_get_ecgtest():
    query = "SELECT id, seq, org_id, site_id, region, edf_path FROM ecgtest;"
    return query