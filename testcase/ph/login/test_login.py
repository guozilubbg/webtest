from selenium import webdriver
import time
import unittest
from page.ph.BasePage import *


class Testlogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = BasePage.url
        self.driver.maximize_window()
        self.page = BasePage(self.driver)
        self.page.get(self.url)

    def tearDown(self):
        self.driver.close()

    def test_login(self):
        # 使用pageObject模式时的web页面自动化测试代码
        # 元素=内容
        self.page.login_username = self.page.lonin_usr
        self.page.login_password = self.page.login_pas
        self.page.login_click.click()
        time.sleep(7)
