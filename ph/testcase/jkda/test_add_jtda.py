"""
新建家庭档案
"""
import time
import unittest
from selenium import webdriver
from ph.page.login_page import *
from ph.data.BaseData import *
from ph.data.jkda_data import *
from ph.page.jkda_page.jtdagl_page import *
from ph.common.Log import Log
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from ph.common.idcard import *

class TestAddJkda(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = Login.url
        self.driver.maximize_window()
        self.page = Login(self.driver)
        self.page.get(self.url)
        self.add = AddJtda(self.driver)

    def tearDown(self):
        # time.sleep(2)
        # self.driver.get_screenshot_as_file(
        #     '//Users//guoxilu//PycharmProjects//webtest//his//pic//%s.jpg' % time.strftime('%Y_%m_%d %H_%M_%S'))

        self.driver.close()

    def test_add_jtda(self):
        # 使用pageObject模式时的web页面自动化测试代码
        # 元素=内容
        time.sleep(1)
        self.page.login_username = BaseData.login_username
        self.page.login_password = BaseData.login_password
        self.page.login_click.click()
        time.sleep(1)
        Log().info("悬浮至健康档案导航栏")
        ActionChains(self.driver).move_to_element(self.add.jkda_dh).perform()
        time.sleep(2)
        Log().info("点击家庭档案按钮")
        ActionChains(self.driver).move_to_element(self.add.jia_ting_dang_an).click().perform()
        time.sleep(3)
        Log().info("点击新增家庭档案按钮")
        self.add.xin_zeng_jia_ting_dang_an.click()
        time.sleep(1)
        Log().info("输入身份证号")
        self.add.jt_shen_fen_zheng_hao = read_excel_xlsx('D:\project\webtest\ph\data\id_card.xlsx', 'Sheet1', "B2")
        time.sleep(1)
        Log().info("点击读卡按钮")
        self.add.jt_du_ka.click()
        time.sleep(1)
        # Log().info("责任医生")
        # self.add.ze_ren_yi_sheng.click()
        # time.sleep(2)
        # Log().info("选择医生")
        # self.add.yi_sheng_xing_ming.click()
        # time.sleep(1)
        Log().info("点击下一步管理家庭成员")
        self.add.xia_yi_bu.click()
        time.sleep(1)
        Log().info("添加家庭成员按钮")
        self.add.tian_jia_jia_ting_cheng_yuan.click()
        time.sleep(1)
        # Log().info("进入from")
        # self.driver.switch_to.frame(self.add.from1)
        # time.sleep(5)
        # Log().info("退出from")
        # self.driver.switch_to.default_content()
        Log().info("输入身份证号码")
        # idcard_list = creatidcard("54")[0]
        # idcard_num = idcard_list[1]
        # idcard_name = idcard_list[0]
        # idcard_tell = idcard_list[2]
        # idcard_address = idcard_list[3]
        self.add.jia_ting_cheng_yuan_sheng_fen_zheng_hao_xpath = '500222198107260026'
        time.sleep(1)
        Log().info("输入姓名")
        self.add.xing_ming = '测试人员'
        time.sleep(1)
        Log().info("点击与户主关系下拉选择框")
        self.add.yu_hu_zhu_guan_xi.click()
        time.sleep(1)
        Log().info("选择配偶")
        self.add.pei_ou.click()
        time.sleep(1)
        Log().info("点击确认按钮")
        self.add.jt_que_ren.click()
        time.sleep(1)
        Log().info("点击完成按钮")
        self.add.jt_wan_cheng.click()
        time.sleep(5)
