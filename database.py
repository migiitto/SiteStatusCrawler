import psycopg2
from psycopg2._psycopg import DatabaseError

from config import DATABASE_IP, DATABASE_PASS, DATABASE_PORT, DATABASE_USER, DATABASE_DB

def get_conn():
    return psycopg2.connect(host=DATABASE_IP, port=DATABASE_PORT, database=DATABASE_DB, user=DATABASE_USER, password=DATABASE_PASS)


def get_cursor(conn):
    """
    Gets cursor with given connection and tests cursor health
    :param conn: Connection
    :return: tested cursor
    """
    curs = conn.cursor()
    try:
        curs.execute('SELECT 1')
    except DatabaseError:
        raise
    return curs