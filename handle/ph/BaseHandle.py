'''
核心操作流程
'''
from data.ph.BaseData import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from common.Log import Log
import time


class BaseHandle():
    # 登录
    def login(self, page, driver=None):
        self.page = page
        self.page.login_username = BaseData.login_username
        # 输入密码
        self.page.login_password = BaseData.login_password
        # 点击登录
        self.page.login_click.click()
        time.sleep(1)

    # 点击服务包
    def click_fam(self, main, driver=None):
        self.main = main
        self.driver = driver
        # 悬浮到家医签约
        ActionChains(self.driver).move_to_element(self.main.fam_fam).perform()
        time.sleep(1)
        # 悬浮到服务内容管理
        ActionChains(self.driver).move_to_element(self.main.fam_pacman).perform()
        time.sleep(1)
        # 悬浮到服务包并点击服务包
        ActionChains(self.driver).move_to_element(self.main.fam_pac_click).click().perform()
        time.sleep(1)

    #  创建服务包
    def creat_new_package(self, creat, main, driver=None):
        self.creat = creat
        Log().info("================================== 悬浮到家医签约 ==================================")

        # # 悬浮到家医签约
        # ActionChains(self.driver).move_to_element(self.main.fam_fam).perform()
        # time.sleep(1)
        # # 悬浮到服务内容管理
        # ActionChains(self.driver).move_to_element(self.main.fam_pacman).perform()
        # time.sleep(1)
        # # 悬浮到服务包并点击服务包
        # ActionChains(self.driver).move_to_element(self.main.fam_pac_click).click().perform()
        # time.sleep(1)
        # 点击新建服务包
        self.creat.fam_crenewpac_click.click()
        time.sleep(1)
        # 输入服务包名字
        self.creat.fam_pacname = BaseData.pacname
        time.sleep(2)
        # 公开级别选取
        self.creat.fam_publiclevel.click()
        time.sleep(5)
        ActionChains(self.creat).move_to_element(self.creat.quyu)

        # Select(self.creat.qu).select_by_index(0)
        # self.creat.quyu.click()
        # 输入服务费
        self.creat.fam_serfee = BaseData.fam_serfee
