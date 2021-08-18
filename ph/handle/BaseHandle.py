'''
核心操作流程
'''
from ph.data.BaseData import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from ph.common.Log import Log
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


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

    # 悬浮服务包
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
        time.sleep(4)

    #  创建服务包
    def creat_new_package(self, creat, driver=None):
        self.creat = creat
        self.driver = driver
        # 点击新建服务包
        self.creat.fam_crenewpac_click.click()
        time.sleep(1)
        # 输入服务包名字
        self.creat.fam_pacname = BaseData.pacname
        write_txt("/Users/guoxilu/PycharmProjects/webtest/ph/data/packagename.txt", "%s\n" % BaseData.pacname, 'a')
        time.sleep(1)
        # 公开级别选取
        self.creat.fam_publiclevel.click()
        time.sleep(4)
        # 选择区域级别
        self.creat.fam_quyu.click()
        # ActionChains(self.driver).move_to_element(self.creat.quyu).click().perform()
        time.sleep(1)
        # 输入服务费
        self.creat.fam_serfee = BaseData.fam_serfee
        time.sleep(1)
        # 保存服务包
        self.creat.fam_save.click()

    # 悬浮到团队管理
    def click_team(self, main, driver=None):
        self.main = main
        self.driver = driver
        # 悬浮到家医签约
        ActionChains(self.driver).move_to_element(self.main.fam_fam).perform()
        time.sleep(1)
        # 悬浮到家医团队管理
        ActionChains(self.driver).move_to_element(self.main.fam_teammanage).perform()
        time.sleep(1)
        # 悬浮到团队管理并点击
        ActionChains(self.driver).move_to_element(self.main.fam_teamadd_click).click().perform()
        time.sleep(1)

    def creat_new_team(self, team, driver=None):
        self.team = team
        self.driver = driver
        # 点击新建团队
        self.team.fam_creatteam_click.click()
        time.sleep(1)
        # 输入团队名称
        self.team.fam_teamname = BaseData.teamname
        write_txt("/Users/guoxilu/PycharmProjects/webtest/ph/data/teamname.txt", "%s\n" % BaseData.teamname, 'a')
        time.sleep(1)
        # 选择隶属机构
        self.team.fam_teamaddr_click.click()
        time.sleep(1)
        # 选择当前机构
        self.team.fam_teamaddr.click()
        time.sleep(1)
        # 添加团队成员
        # 切记表单
        self.driver.switch_to.frame(self.team.fam_teamadd_form)
        time.sleep(1)
        # 点击下拉框
        self.team.fam_addmember_click.click()
        time.sleep(1)
        # 退出表单
        self.driver.switch_to.default_content()
        time.sleep(1)
        # 选择成员1
        ActionChains(self.driver).move_to_element(self.team.fam_member1).click().perform()
        # self.team.fam_member1.click()
        time.sleep(1)
        # 点击添加
        self.team.fam_add_click.click()
        time.sleep(1)
        '''
        需要做个判断，看是否弹出提示框，还要做个循环，判断添加团队成员个数
        '''
        # 如果弹出提示，选择继续添加
        self.team.fam_goon.click()
        time.sleep(2)
        # 切近表单，添加成员二
        self.driver.switch_to.frame(self.team.fam_teamadd_form)
        time.sleep(1)
        self.team.fam_addmember_click.click()
        time.sleep(1)
        # 退出表单
        self.driver.switch_to.default_content()
        self.team.fam_member2.click()
        time.sleep(1)
        self.team.fam_add_click.click()
        time.sleep(1)
        self.team.fam_goon.click()
        time.sleep(1)
        # 选择负责人
        self.team.fam_leader_click.click()
        time.sleep(1)
        # 分配团队角色
        # self.team.fam_role1_click.click()
        # time.sleep(1)
        # self.team.fam_famdoc_click.click()
        # time.sleep(1)
        # self.team.fam_role2_click.click()
        # time.sleep(1)
        # self.team.fam_nurse_click.click()
        # time.sleep(1)
        # 保存
        self.team.fam_save.click()
        self.team.fam_save_goon.click()
        time.sleep(1)

    # 悬浮到成员管理
    def click_addmember(self, main, driver=None):
        self.main = main
        self.driver = driver
        # 悬浮到家医签约
        ActionChains(self.driver).move_to_element(self.main.fam_fam).perform()
        time.sleep(1)
        # 悬浮到家医团队管理
        ActionChains(self.driver).move_to_element(self.main.fam_teammanage).perform()
        time.sleep(1)
        # 悬浮到团队管理并点击
        ActionChains(self.driver).move_to_element(self.main.fam_teammembers_click).click().perform()
        time.sleep(1)

    # 添加成员
    def add_members(self, add, driver=None):
        self.add = add
        self.driver = driver
        # 点击添加成员
        self.add.fam_addmem_click.click()
        time.sleep(1)
        # 点击搜索用户
        self.add.fam_selectmem_click.click()
        # 获取li个数
        '''
        后期完善通过判断li个数来添加成员
        '''
        self.add.fam_mem_click.click()

        # 选择权限机构
        # 输入服务级别
        # 团队角色
        # 保存
        time.sleep(1)

    # 悬浮到家庭签约
    def click_famsigning(self, main, driver=None):
        self.main = main
        self.driver = driver
        # 悬浮到家医签约
        ActionChains(self.driver).move_to_element(self.main.fam_fam).perform()
        time.sleep(1)
        # 悬浮到家医团队管理
        ActionChains(self.driver).move_to_element(self.main.fam_signing).perform()
        time.sleep(1)
        # 悬浮到团队管理并点击
        ActionChains(self.driver).move_to_element(self.main.fam_famsigning_click).click().perform()
        time.sleep(1)

    def famsigning(self, fam, driver=None):
        self.fam = fam
        self.driver = driver
        #点击签约
        self.fam.fam_famsigning_click.click()
        time.sleep(1)
        #选择服务类型
        self.driver.switch_to.frame(self.fam.fam_sig_form)
        self.fam.fam_sigtype_click.click()
        time.sleep(1)
        self.driver.switch_to.default_content()
        self.fam.fam_sigtype2.click()
        time.sleep(1)
        #签发机构
        self.driver.switch_to.frame(self.fam.fam_sig_form)
        self.fam.fam_signong.click()
        time.sleep(1)
        self.driver.switch_to.default_content()
        self.fam.fam_sigadd1.click()
        time.sleep(1)
        #服务团队
        self.driver.switch_to.frame(self.fam.fam_sig_form)
        self.fam.fam_sigteam.click()
        time.sleep(1)
        self.driver.switch_to.default_content()
        self.fam.fam_sigteam2.click()
        time.sleep(10)
        #签约服务家庭
        self.driver.switch_to.frame(self.fam.fam_sig_form)
        self.fam.fam_fam = BaseData.idcardnum
        time.sleep(1)
        self.driver.switch_to.default_content()
        self.fam.fam_fam_clck.click()
        time.sleep(1)
        #签约服务包
        self.driver.switch_to.frame(self.fam.fam_sig_form)
        self.fam.fam_servicePackCode_click.click()
        time.sleep(1)
        self.driver.switch_to.default_content()
        self.fam.fam_servicePackCode1.click()
        time.sleep(1)
        #保存
        self.driver.switch_to.frame(self.fam.fam_sig_form)
        self.fam.fam_save.click()
        self.fam.fam_save_goon.click()
        time.sleep(1)
