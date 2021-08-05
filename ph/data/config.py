'''
基础数据
'''

class BaseConf(object):
    # mysql配置信息
    MYSQL_HOST = "172.16.19.106"
    MYSQL_PORT = "3306"
    MYSQL_USER = "admin"
    MYSQL_PWD = "Admin!123"
    MYSQL_DB = 'test_br_sc_his_20210421'

    # url
    public_health_url = "http://172.16.19.227/dashboard/workplace"#"http://172.16.19.203:9081/login"

    TIMEOUT = 12  # 元素等待超时时间

    exists = 10  # 元素存在等待时间

