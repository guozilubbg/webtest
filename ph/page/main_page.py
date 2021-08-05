'''
导航页面
'''
from ph.common.PageObject import PageObject, PageElement
from ph.data.config import *


class Main_Page(PageObject):
    # 点击桌面添加
    fam_add = PageElement(
        xpath='//*[@id="app"]/section/section/main/div/div/div/div[2]/div/div[2]/div/div[2]/div[1]/div[2]/div/button')

    # 点击全民健康
    fam_doc = PageElement(xpath='//*[@id="app"]/section/section/header/div/div/div[2]/ul/li[8]')

    # 查找家医签约字段
    fam_fam = PageElement(xpath='//*[@id="app"]/section/section/header/div/div/div[2]/ul/li[10]/div/span/span/span')

    # 查找服务内容管理
    fam_pacman = PageElement(xpath='/html/body/div[2]/div/div/ul/li[1]/div[1]/span/span/span')

    # 查找服务包
    fam_pac_click = PageElement(xpath='/html/body/div[2]/div/div/ul/li[1]/div[2]/div/div/ul/li/a/span')
