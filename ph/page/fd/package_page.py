'''
服务包页面
'''
from ph.common.PageObject import PageObject, PageElement
from ph.data.config import *


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
    fam_quyu = PageElement(xpath='//*[@class="ant-select-dropdown ant-select-dropdown--single ant-select-dropdown-placement-bottomLeft"]/div/ul/li[1]')
    fam_benji = PageElement(xpath='//*[@class="ant-select-dropdown ant-select-dropdown--single ant-select-dropdown-placement-bottomLeft"]/div/ul/li[2]')

    #签约服务费
    fam_serfee = PageElement(xpath='//*[@id="serviceCharge"]/div[2]/input')

    #保存
    fam_save = PageElement(xpath='//*[@id="app"]/section/section/main/div/div/div/div[2]/div/div/div/div/div/div/button[1]')


