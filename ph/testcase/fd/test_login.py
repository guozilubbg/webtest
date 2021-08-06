from selenium import webdriver
import unittest
from ph.page.login_page import *
from ph.data.BaseData import *


class TestLogIn(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = Login.url
        self.driver.maximize_window()
        self.page = Login(self.driver)
        self.page.get(self.url)


    def tearDown(self):
        time.sleep(2)
        self.driver.get_screenshot_as_file(
            '//Users//guoxilu//PycharmProjects//webtest//his//pic//%s.jpg' % time.strftime('%Y_%m_%d %H_%M_%S'))

        self.driver.close()

    def test_login(self):
        # 使用pageObject模式时的web页面自动化测试代码
        # 元素=内容
        self.page.login_username = BaseData.login_username
        self.page.login_password = BaseData.login_password
        self.page.login_click.click()
        time.sleep(8)

        #断言







