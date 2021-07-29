'''
业务层，封装好了的login步骤
'''
from handle.login_handle import LoginHandle
import time
from config.data import username,password


class LoginBusiness:
    def __init__(self, driver):
        self.driver = driver
        self.login_handle = LoginHandle(self.driver)

    def login_pass(self):
        self.login_handle.send_username(username)
        self.login_handle.send_password(password)
        self.login_handle.click_login()

    def login_user_error(self):
        self.login_handle.send_username('18821768011')
        self.login_handle.send_password('111111')
        self.login_handle.click_login()
        user_flag = self.login_handle.get_fail_tost('帐号未注册')
        if user_flag:
            return True
        else:
            return False

    def login_password_error(self):
        self.login_handle.send_username('18821768014')
        self.login_handle.send_password('111112')
        self.login_handle.click_login()
        user_flag = self.login_handle.get_fail_tost('登陆密码错误')
        if user_flag:
            return True
        else:
            return False

    def go_paizhao(self):
        self.login_handle.click_paizhao()

    def go_tianqi(self):
        self.login_handle.click_tianqi()

    def go_baidu(self):
        self.login_handle.click_baidu()