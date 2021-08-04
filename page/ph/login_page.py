'''
登录模块的定位元素
'''
from common.pageObject import PageObject, PageElement
from data.url import *
from data.ph.BaseData import *
from selenium import webdriver


class Login(PageObject):
    # 当前测试页面的测试网址url
    base_url = Url.public_health_url
    url = base_url + '/'

    driver = webdriver.Chrome()

    # 查询登录元素
    login_username = PageElement(id="username")
    login_password = PageElement(id="password")
    # 点击登录
    login_click = PageElement(id="loginBtn")

    #核心操作流程
    def lohin(self, url, username, password):
        self.get(url)


