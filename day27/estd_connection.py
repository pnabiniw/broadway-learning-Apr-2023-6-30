# mysqlclient package is the connector for connection between python and MySQL Database
# psycopg2 is the connector for connection between python and Postgres

import psycopg2


def estd_connection():
    conn = psycopg2.connect(
        database='pystudent',
        user='postgres',
        password='password',
        host='127.0.0.1',
        port=5432
    )

    conn.autocommit = True
    print("Connection established successfully !!")
    cursor = conn.cursor()
    return cursor
