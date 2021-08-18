'''
团队管理页面
'''
from ph.common.PageObject import PageObject, PageElement
from ph.data.config import *


class Team_Page(PageObject):
    # 当前测试页面的测试网址url，目前操作是基于登录后的操作
    # base_url = Url.public_health_url
    # url = base_url + '/'

    #点击新建团队
    fam_creatteam_click = PageElement(xpath='//*[@id="app"]/section/section/main/div/div/div/div[2]/div/div/div/div[1]/div[1]/div/div[1]/button')

    # 输入团队名称
    fam_teamname = PageElement(id='teamName')

    # 选择隶属机构
    fam_teamaddr_click = PageElement(xpath='/html/body/div[1]/section/section/main/div/div/div/div[2]/div/div/div/div/form/div[1]/div[3]/div/div[2]/div/span/div/div')
    fam_teamaddr = PageElement(xpath='//*[@class="ant-select-dropdown ant-select-dropdown--single ant-select-dropdown-placement-bottomLeft"]/div/ul/li')

    # 添加团队成员
    fam_teamadd_form = PageElement(class_name='thick-form ant-form ant-form-horizontal')
    fam_addmember_click = PageElement(xpath='//*[@class="ant-card-head-wrapper"]/div/div/div[1]/div/div')
    fam_member1 = PageElement(xpath='//*[@class="ant-select-dropdown-menu-item ant-select-dropdown-menu-item-active"]')
    fam_member2 = PageElement(xpath='//*[@class="ant-select-dropdown ant-select-dropdown--single ant-select-dropdown-placement-bottomLeft"]/div/ul/li[2]')
    fam_add_click = PageElement(xpath='//*[@id="app"]/section/section/main/div/div/div/div[2]/div/div/div/div/div[1]/div[1]/div/div[2]/div/button')
    fam_goon = PageElement(xpath='//*[@class="ant-modal-root ant-modal-confirm ant-modal-confirm-confirm ant-modal-confirm ant-modal-confirm-confirm ant-modal-confirm"]/div[2]/div/div[2]/div/div/div[2]/button[2]')

    # 选择负责人
    fam_leader_click = PageElement(xpath='//*[@id="app"]/section/section/main/div/div/div/div[2]/div/div/div/div/div[1]/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[7]/span/label/span/input')

    # 分配团队角色
    '''
    div会随着人员的增多而增多
    '''
    fam_role1_click = PageElement(xpath='//*[@id="app"]/section/section/main/div/div/div/div[2]/div/div/div/div/div[1]/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[8]/span/div/div')
    fam_role2_click = PageElement(xpath='//*[@id="app"]/section/section/main/div/div/div/div[2]/div/div/div/div/div[1]/div[2]/div/div/div/div/div/div/table/tbody/tr[2]/td[8]/span/div/div')
    fam_famdoc_click = PageElement(xpath='//*[@class="ant-select-dropdown ant-select-dropdown--single ant-select-dropdown-placement-topLeft"]/div/ul/[@class="ant-select-dropdown-menu-item ant-select-dropdown-menu-item-selected"]')
    fam_nurse_click = PageElement(xpath='//*[@class="ant-select-dropdown ant-select-dropdown--single ant-select-dropdown-placement-topLeft"]/div/ul/li[2]')
    # 保存
    fam_save = PageElement(xpath='/html/body/div[1]/section/section/main/div/div/div/div[2]/div/div/div/div/div[2]/div/button[1]')
    fam_save_goon = PageElement(xpath='//*[@class="ant-modal-confirm-btns"]/button[2]')