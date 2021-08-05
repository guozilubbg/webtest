'''
服务包页面
'''
from common.PageObject import PageObject, PageElement
from data.url import *


class Package_Page(PageObject):
    # 当前测试页面的测试网址url，目前操作是基于登录后的操作
    # base_url = Url.public_health_url
    # url = base_url + '/'

    # 点击新建服务包
    fam_crenewpac_click = PageElement(
        xpath='//*[@id="app"]/section/section/main/div/div/div/div[2]/div/div/div/div[1]/div[1]/div/div[1]/button')

    # 服务包名称
    fam_pacname = PageElement(xpath='//*[@id="servicePackName"]')

    #定位到公开级别下拉框
    fam_publiclevel = PageElement(xpath='//*[@id="servicePackPublicLevel"]')

    #公开级别
    quyu = PageElement(xpath='//*[@class="ant-select-dropdown-menu ant-select-dropdown-menu-vertical ant-select-dropdown-menu-root"]/ul/li[1]')
    fam_levsvg = PageElement(xpath='//*[@id="20be5ae8-4063-4fd2-86a9-861233c482ef"]/ul')

    #签约服务费
    fam_serfee = PageElement(xpath='//*[@id="serviceCharge"]/div[2]/input')