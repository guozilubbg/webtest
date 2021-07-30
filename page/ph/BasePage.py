from common.pageObject import PageObject, PageElement
from data.url import *
from data.ph.BaseData import *


class BasePage(PageObject):
    # 当前测试页面的测试网址url
    base_url = Url.public_health_url
    url = base_url + '/'

    # 查询登录元素
    login_username = PageElement(id="username")
    login_password = PageElement(id="password")
    #点击登录
    login_click = PageElement(id="loginBtn")

    #输入元素
    lonin_usr = BaseData.login_username
    login_pas = BaseData.login_password

    #点击桌面添加
    fam_add = PageElement(xpath='//*[@id="app"]/section/section/main/div/div/div/div[2]/div/div[2]/div/div[2]/div[1]/div[2]/div/button')

    #点击全民健康
    fam_doc = PageElement(xpath='//*[@id="app"]/section/section/header/div/div/div[2]/ul/li[8]')



