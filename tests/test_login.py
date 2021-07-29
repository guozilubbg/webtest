
import unittest
# from page.login import *
from selenium import webdriver
from common.logger import Log
from business.login_buginess import LoginBusiness
import time
from config.data import url

class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls, value=url):
        cls.driver = webdriver.Chrome()
        cls.driver.get(value)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(30)
        cls.log = Log()
        cls.login_business = LoginBusiness(cls.driver)

    def tearDown(cls):
        cls.driver.quit()

    def test_01(cls):
        time.sleep(5)
        cls.log.info("------登录失败用例：start!---------")
        # self.login_business.login_pass()
        # self.login_business.go_paizhao()
        cls.login_business.go_baidu()

# self.assertNotEqual(1,2)
# self.assertTrue(flag)
# self.assertFalse(flag)


# @unittest.skip("CaseTest")
# def test_02(self):
# 	self.login_business.login_user_error()
# 	print ("this is case02\n")	def tearDown(self):
# 		self.driver.quit()
# 	self.assertTrue(True)

if __name__ == '__main__':
    unittest.main(verbosity=2)
