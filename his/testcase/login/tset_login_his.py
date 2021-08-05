'''
功能：测试his的登录
'''

import unittest
from selenium import webdriver
from his.data.BaseData import *
from his.page.system_page_his import *
from selenium.webdriver.common.action_chains import ActionChains
from his.common.Log import Log
from his.util.decorator import screenshot

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = AddHospital.url
        self.driver.maximize_window()
        self.page = AddHospital(self.driver)
        self.page.get(self.url)



    def tearDown(self):
        self.driver.close()

    @screenshot
    def test_login(self):
        # 使用pageObject模式时的web页面自动化测试代码
        # 元素=内容
        Log().info("点击用户栏并输入用户名")
        self.page.his_username = BaseData.his_login_username
        time.sleep(1)
        Log().info("点击密码栏栏并输入密码")
        self.page.his_password = BaseData.his_login_password
        time.sleep(1)
        Log().info("点击登录按钮")
        self.page.his_loginbutton.click()
        # BaseHandleHis().login_his(self.page
        time.sleep(3)
        Log().info("点击导航栏系统管理按钮")
        self.page.his_system.click()
        time.sleep(4)
        # Log().info("点击医院管理-增加按钮")
        self.driver.switch_to.frame(self.page.hos_frame)
        time.sleep(1)
        self.page.his_add_hos.click()
        # Log().info("悬浮到增加按钮")
        # ActionChains(self.driver).move_to_element(self.page.his_add_hos).click().perform()
        # time.sleep(1)

        time.sleep(10)






