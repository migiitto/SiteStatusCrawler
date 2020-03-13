import datetime

import psycopg2

from checker.CheckerConf import CheckerConf
from database.database import get_cursor, get_conn


def get_sites():
    list_of_sites = []
    conn = None
    try:
        conn = get_conn()
        cursor = get_cursor(conn)
        cursor.execute("SELECT id, name, url, frequency, regex FROM sites")


        for row in cursor.fetchall():
            list_of_sites.append(CheckerConf.fromSQL(row))

        cursor.close()
    except (Exception, psycopg2.DatabaseError) as e:
        print(e)
    finally:
        if conn is not None:
            conn.close()  # Closing connection should close cursor as well.
    return list_of_sites

def insert_record(conf, response_code, response_time, valid, timechecked):
    conn = None
    try:
        conn = get_conn()
        cursor = get_cursor(conn)
        cursor.execute(
            "INSERT INTO sites_stats(site_id, response_code, timestamp, response_time, response_pass) VALUES(%s, %s, TIMESTAMP %s, %s, %s)",
            (conf.id, response_code, str(timechecked), int(response_time*1000), valid))
        conn.commit()
        print("Committed rows")
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as e:
        print(e)
    finally:
        if conn is not None:
            conn.close()  # Closing connection should close cursor as well.
