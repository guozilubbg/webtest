'''
功能：新建一个正确的服务包
'''
from selenium import webdriver
import unittest
from page.ph.login_page import *
from data.ph.BaseData import *
from page.ph.main_page import *
from page.ph.package_page import *
from handle.ph.BaseHandle import *

class TestCreateNewPackage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        # self.url = Login.url
        # self.driver.maximize_window()
        # self.page = Login(self.driver)
        # self.page.get(self.url)
        # self.main = main(self.driver)
        # self.creat = Package(self.driver)


    def tearDown(self):
        self.driver.close()

    def test_creatnewpackage(self):
        BaseHandle.login()
        BaseHandle.creat_new_package()
        # 使用pageObject模式时的web页面自动化测试代码
        # 元素:内容
        # 输入账号
        # self.page.login_username = BaseData.login_username
        # #输入密码
        # self.page.login_password = BaseData.login_password
        # # 点击登录
        # self.page.login_click.click()
        # time.sleep(1)
        # #悬浮到家医签约
        # ActionChains(self.driver).move_to_element(self.main.fam_fam).perform()
        # time.sleep(1)
        # #悬浮到服务内容管理
        # ActionChains(self.driver).move_to_element(self.main.fam_pacman).perform()
        # time.sleep(1)
        # #悬浮到服务包并点击服务包
        # ActionChains(self.driver).move_to_element(self.main.fam_pac_click).click().perform()
        # time.sleep(1)
        # #点击新建服务包
        # self.creat.fam_crenewpac_click.click()
        # time.sleep(1)
        # #输入服务包名字
        # self.creat.fam_pacname = BaseData.pacname
        # time.sleep(2)
        # #公开级别选取
        # self.creat.fam_publiclevel.click()
        # time.sleep(5)
        # ActionChains(self.creat).move_to_element(self.creat.quyu)
        #
        # # Select(self.creat.qu).select_by_index(0)
        # # self.creat.quyu.click()
        # #输入服务费
        # self.creat.fam_serfee = BaseData.fam_serfee




        time.sleep(100)




