import pymysql
from his.data.config import *

host = BaseConf.MYSQL_HOST
port = int(BaseConf.MYSQL_PORT)
user = BaseConf.MYSQL_USER
pwd = BaseConf.MYSQL_PWD
db = BaseConf.MYSQL_DB


class MysqlDb(object):
    def select_yiyuan(self):
        con = pymysql.connect(host=host, port=port, user=user, passwd=pwd, charset='utf8')
        con.select_db(db)
        sql = '''
        select * from yi_yuan;
        '''
        cur = con.cursor()#创建游标

        cur.execute(sql)#执行游标里的语句
        while 1:
            res = cur.fetchone()
            if res is None:
                # 表示已经取完结果集
                break
            print(res)
        cur.close()
        con.commit()#提交数据库
        con.close()#关闭数据库
        print('sql执行成功')
