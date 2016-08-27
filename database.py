import pymysql
from pymysql import MySQLError
import CONFIG


def insert_to_database(title, lat, long, url):
    conn = \
        pymysql.connect(host='CONFIG.SQL_HOST'
                        , user='CONFIG.USER', passwd='CONFIG.PASS',
                        db='CONFIG.DB_NAME')
    cur = conn.cursor()
    try:
        cur.execute(CONFIG.INSERT_COMMAND + "'" + title + "','" + lat + "','" + long + "','" + url + "')")
        conn.commit()
        print('Database Success')
    except MySQLError as e:
        pass
