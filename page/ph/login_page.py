'''
登录模块的定位元素
'''
from common.PageObject import PageObject, PageElement
from data.url import *
from selenium import webdriver


class Login(PageObject):
    # 当前测试页面的测试网址url
    base_url = Url.public_health_url
    url = base_url + '/'

    # 查询登录元素
    login_username = PageElement(id="username")
    login_password = PageElement(id="password")
    # 点击登录
    login_click = PageElement(id="loginBtn")





