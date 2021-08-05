'''
核心操作流程
'''
from his.data.BaseData import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from his.common.Log import Log
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

