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
        # Fix UTF-8 problem
        cur.execute(CONFIG.ALTER_DB)
        # Start inserting into the database
        cur.execute(CONFIG.INSERT_COMMAND + "'" + title.strip() + "','" + lat + "','" + lon + "','" + url + "')")
        conn.commit()
        print('Database Success')
    except MySQLError as e:
        print(e)
        pass
