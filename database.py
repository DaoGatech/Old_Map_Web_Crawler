import pymysql
from pymysql import MySQLError
import CONFIG


def insert_to_database(title, lat, lon, url):
    try:
        conn = \
            pymysql.connect(host=CONFIG.SQL_HOST
                            , user=CONFIG.USER, passwd=CONFIG.PASS,
                            db=CONFIG.DB_NAME, charset='utf8')
        cur = conn.cursor()
        print(CONFIG.INSERT_COMMAND + "'" + title + "','" + lat + "','" + lon + "','" + url + "')")
        cur.execute(CONFIG.INSERT_COMMAND + "'" + title + "','" + lat + "','" + lon + "','" + url + "')")
        conn.commit()
        print('Database Success')
    except MySQLError as e:
        print(e)
        pass
