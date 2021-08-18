'''
功能：添加成员
'''
import unittest
from ph.page.login_page import *
from ph.page.main_page import *
from ph.page.fd.addmembers_page import *
from ph.handle.BaseHandle import *


class TestAddMember(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = Login.url
        self.driver.maximize_window()
        self.page = Login(self.driver)
        self.page.get(self.url)
        self.main = Main_Page(self.driver)
        self.add = Members_Page(self.driver)

    def tearDown(self):
        # time.sleep(2)
        # self.driver.get_screenshot_as_file(
        #     '//Users//guoxilu//PycharmProjects//webtest//his//pic//%s.jpg' % time.strftime('%Y_%m_%d %H_%M_%S'))
        self.driver.close()
    @unittest.skip('跳过添加成员用例')
    def test_addmembers(self):
        # Log().info("==================测试：添加成员==================================")
        BaseHandle().login(page=self.page)
        BaseHandle().click_addmember(main=self.main, driver=self.driver)
        BaseHandle().add_members(add=self.add, driver=self.driver)
