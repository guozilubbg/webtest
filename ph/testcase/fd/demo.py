import time

from ph.common.Base import *
from selenium import webdriver


class login(Base):
    url = "http://172.16.19.202:8080/his/"
    user = (By.ID, "userName")
    password = (By.ID, "password")
    login_button = (By.CLASS_NAME, "login_button")

    def lohin(self, user, passw):
        self.visit(self.url)
        time.sleep(5)
        self.input(self.user,user)
        self.input(self.password,passw)
        time.sleep(2)
        self.click(self.login_button)
        time.sleep(44)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    his_login_username = "XT001"
    his_login_password = "123"
    lp = login(driver)
    lp.lohin(his_login_username, his_login_password)
