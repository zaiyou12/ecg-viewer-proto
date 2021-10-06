def get_ecg_tests():
    sql = f"""
        SELECT * FROM ecg_test ORDER BY start_time
        LIMIT 20
    """
    return sql
