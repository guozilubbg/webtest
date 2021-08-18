'''
新建健康档案
'''
import time
import unittest
from selenium import webdriver
from ph.page.login_page import *
from ph.data.BaseData import *
from ph.data.jkda_data import *
from ph.page.jkda_page.jkdagl_page import *
from ph.common.Log import Log
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from ph.common.idcard import read_excel_xlsx, creatidcard


class TestAddJkda(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = Login.url
        self.driver.maximize_window()
        self.page = Login(self.driver)
        self.page.get(self.url)
        self.add = AddJkda(self.driver)

    def tearDown(self):
        # time.sleep(2)
        # self.driver.get_screenshot_as_file(
        #     '//Users//guoxilu//PycharmProjects//webtest//his//pic//%s.jpg' % time.strftime('%Y_%m_%d %H_%M_%S'))

        self.driver.close()

    def test_add_jkda(self):
        # 使用pageObject模式时的web页面自动化测试代码
        # 元素=内容、
        time.sleep(1)
        self.page.login_username = BaseData.login_username
        self.page.login_password = BaseData.login_password
        self.page.login_click.click()
        time.sleep(1)

        Log().info("悬浮至健康档案导航栏")
        ActionChains(self.driver).move_to_element(self.add.jkda_dh).perform()
        time.sleep(1)
        Log().info("点击快速建档按钮")
        ActionChains(self.driver).move_to_element(self.add.kuai_su_jian_dang).click().perform()
        time.sleep(1)
        Log().info("输入身份证号码")
        creatidcard("54")
        # idcard_num1 = idcard_list1[1]
        # idcard_name1 = idcard_list1[0]
        # idcard_tell1 = idcard_list1[2]
        # idcard_address1 = idcard_list1[3]
        time.sleep(3)
        self.add.shen_feng_zheng_hao = JkdaData.ju_ming_shen_fen_zheng_hao
        # 获取嵌套列表中的数据也可用以下方法
        # self.add.shen_feng_zheng_hao = creatidcard('54')[0][1]
        time.sleep(1)
        Log().info("输入姓名")
        self.add.name = JkdaData.ju_min_xing_ming
        time.sleep(1)
        Log().info("输入电话号码")
        self.add.tell = JkdaData.ju_ming_dian_hua
        time.sleep(1)
        Log().info("选择户籍地")
        self.add.hu_ji_di.click()
        time.sleep(1)
        Log().info("选择北京市")
        self.add.bei_jin_shi.click()
        time.sleep(1)
        Log().info("选择东城区")
        self.add.dong_cheng_qu.click()
        self.add.kong_bai1.click()
        time.sleep(1)
        Log().info("选择户籍地详细地址")
        self.add.hu_ji_di_xiang_xi = JkdaData.hu_ji_di_xiang_xi_di_zhi
        time.sleep(1)
        Log().info("选择工作单位")
        self.add.gong_zuo_dan_wei = JkdaData.ju_min_gong_zuo_dan_wei
        time.sleep(1)
        Log().info("选择居住地")
        self.add.ju_zhu_di.click()
        self.add.xi_zang_zi_zi_qu.click()
        self.add.chang_du_shi.click()
        self.add.ka_ruo_qu.click()
        self.add.ka_ruo_zheng.click()
        self.add.ka_ruo_zheng_cuo_ming_wei_yuan_hui.click()
        time.sleep(1)
        Log().info("选择居住地详细地址")
        self.add.ju_zhu_di_xiang_xi = JkdaData.ju_zhu_di_xiang_xi_di_zhi
        time.sleep(1)
        Log().info("点击完成建档按钮")
        self.add.wan_cheng_jian_dang.click()
        time.sleep(1)
        # Log().info("断言是否完成建档")
        # self.assertEqual(self.add.da_yin_dang_an.text, JkdaData.da_yin_dang_an, 'ok')
        # time.sleep(1)
        Log().info("点击返回列表")
        self.add.fan_hui_lie_biao.click()
        time.sleep(1)
