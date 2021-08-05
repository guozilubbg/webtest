'''
mysql数据库
'''
import logging
from ph.data.config import *
import pymysql as sql


class MysqlDb(object):
    host = BaseConf.MYSQL_HOST
    port = int(BaseConf.MYSQL_PORT)
    user = BaseConf.MYSQL_USER
    pwd = BaseConf.MYSQL_PWD
    db = BaseConf.MYSQL_DB

    def __init__(self):
        self.conn = sql.connect(host=self.host, port=self.port,
                                user=self.user, passwd=self.pwd, charset='utf8')
        self.cursor = self.conn.cursor(dictionary=True)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cursor is not None:
            self.cursor.close()
        if self.conn is not None:
            self.conn.close()
        if exc_tb:
            print("error: ".format(str(exc_val)))

    def close(self):
        self.cursor.close()
        self.conn.close()

    def query(self, sql, params=()):
        rv = None
        cursor = self.cursor
        try:
            cursor.execute(sql, params)
            rv = cursor.fetchall()
        except Exception as err:
            logging.error('query error: {}'.format(str(err)))
            print(str(err))
        return rv

    def operator(self, sql, params=()):
        rv = False
        cursor = self.cursor()
        try:
            cursor.execute(sql, params)
            self.conn.commit()
            rv = True
        except Exception as err:
            logging.error('query error: {}'.format(str(err)))
            print(str(err))
        return rv
