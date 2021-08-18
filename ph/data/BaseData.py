'''
测试数据
'''
import random
import time
from ph.common.Base import *
from ph.data.address import *


class BaseData:
    # 公卫登录账号密码
    login_username = "13908958297"
    login_password = "111111"
    # his登录账号密码
    his_login_username = "XT001"
    his_login_password = "123"
    # 获取当前时间戳
    time_now = int(time.time())
    # 服务包名字
    pacname = "测试包%s" % time_now
    # 服务包价格
    fam_serfee = "%s" % random.randint(1, 10000)
    # 新建团队名称
    teamname = "团队%s" % time_now
    # 从txt中拿出数据
    team_name = read_txt('/Users/guoxilu/PycharmProjects/webtest/ph/data/teamname.txt', "r")
    pac_name = read_txt('/Users/guoxilu/PycharmProjects/webtest/ph/data/packagename.txt', "r")
    #身份证号
    idcardnum = "500114197706140018"

