from selenium import webdriver
import time
import unittest
from page.ph.login_page import *
from data.ph.BaseData import *


class TestLogIn(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = login.url
        self.driver.maximize_window()
        self.page = login(self.driver)
        self.page.get(self.url)


    def tearDown(self):
        self.driver.close()

    def test_login(self):
        # 使用pageObject模式时的web页面自动化测试代码
        # 元素=内容
        self.page.login_username = BaseData.login_username
        self.page.login_password = BaseData.login_password
        self.page.login_click.click()
        time.sleep(8)





