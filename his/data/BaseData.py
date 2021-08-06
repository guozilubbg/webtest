'''
测试数据
'''
import time

class BaseData:
    #公卫登录账号密码
    login_username = "13908958297"
    login_password = "111111"
    #his登录账号密码
    his_login_username = "001"
    his_login_password = "123"

    #获取当前时间戳
    time_now = int(time.time())
    # 服务包名字
    pacname = "测试包%s"%time_now

    #service fee
    fam_serfee = "123"
