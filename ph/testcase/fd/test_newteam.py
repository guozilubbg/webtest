'''
功能：新建团队
'''
import unittest
from ph.page.login_page import *
from ph.page.main_page import *
from ph.page.fd.teamadd_page import *
from ph.handle.BaseHandle import *


class TestCreateNewTeam(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = Login.url
        self.driver.maximize_window()
        self.page = Login(self.driver)
        self.page.get(self.url)
        self.main = Main_Page(self.driver)
        self.team = Team_Page(self.driver)

    def tearDown(self):
        # time.sleep(2)
        # self.driver.get_screenshot_as_file(
        #     '//Users//guoxilu//PycharmProjects//webtest//his//pic//%s.jpg' % time.strftime('%Y_%m_%d %H_%M_%S'))
        self.driver.close()

    def test_creatnewteam(self):
        # Log().info("==================测试：新建团队==================================")
        BaseHandle().login(page=self.page)
        BaseHandle().click_team(main=self.main, driver=self.driver)
        BaseHandle().creat_new_team(team=self.team, driver=self.driver)