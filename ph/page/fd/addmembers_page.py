'''
团队管理页面
'''
from ph.common.PageObject import PageObject, PageElement
from ph.data.config import *


class Members_Page(PageObject):
    # 当前测试页面的测试网址url，目前操作是基于登录后的操作
    # base_url = Url.public_health_url
    # url = base_url + '/'

    #点击添加成员
    fam_addmem_click = PageElement(xpath='//*[@id="app"]/section/section/main/div/div/div/div[2]/div/div/div/div[1]/div[1]/div/div[1]/button')

    # 点击搜索用户
    fam_selectmem_click = PageElement(xpath='//*[@id="app"]/section/section/main/div/div/div/div[2]/div/div/div/div/form/div[1]/div[1]/div/div[2]/div/span/div/div')
    fam_mem_click = PageElement(xpath='//*[@id="40cb23a9-a519-4e2e-aa62-a58f066ac6d2"]/ul')

    # 选择权限机构
    # 输入服务级别
    # 团队角色
    # 保存