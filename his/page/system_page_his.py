'''
his系统管理界面定位元素
'''
import time

from his.common.PageObject import PageElement,PageObject
from his.data.config import *
class AddHospital(PageObject):
    # # 当前测试页面的测试网址url
    # base_url = Url.his_health_url
    # url = base_url + '/'

    base_url = BaseConf.his_health_url
    url = base_url + '/'

    # 账号
    his_username = PageElement(id="userName")

    his_password = PageElement(id="password")

    his_loginbutton = PageElement(class_name="login_button")
    #系统管理按钮
    his_system = PageElement(xpath='//*[@id="pf-hd"]/div[2]/div[1]/div/ul/li[2]/a/span[2]')
    #进入医院frame界面
    hos_frame = PageElement(xpath='//*[@id="pf-page"]/div[2]/div[2]/div/div/iframe')
    #医院管理-增加按钮
    his_add_hos = PageElement(xpath='/html/body/div[1]/div[1]/div/div/div/div[1]/div[2]/span/a[1]')