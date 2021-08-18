'''
健康档案管理
'''
from ph.common.PageObject import PageObject, PageElement
from ph.data.config import *

class AddJkda(PageObject):
    #健康档案导航按钮
    jkda_dh = PageElement(xpath='/html/body/div[1]/section/section/header/div/div/div[2]/ul/li[4]/div/span/span/span')
    #快速建档按钮
    kuai_su_jian_dang = PageElement(xpath='/html/body/div[2]/div/div/ul/li[1]/a')
    #身份证输入框
    shen_feng_zheng_hao = PageElement(xpath='//*[@id="sfzhm"]')
    #姓名输入框
    name = PageElement(xpath='/html/body/div[1]/section/section/main/div/div/div/div[2]/div/div/div[2]/div[1]/div/div/div[2]/form/div[1]/div[2]/div/div[2]/div/span/input')
    #电话输入框
    tell = PageElement(xpath='/html/body/div[1]/section/section/main/div/div/div/div[2]/div/div/div[2]/div[1]/div/div/div[2]/form/div[3]/div[1]/div/div[2]/div/span/input')
    #工作单位输入框
    gong_zuo_dan_wei = PageElement(xpath='/html/body/div[1]/section/section/main/div/div/div/div[2]/div/div/div[2]/div[1]/div/div/div[2]/form/div[4]/div[1]/div/div[2]/div/span/input')
    #户籍地修改按钮和详细地址
    hu_ji_di = PageElement(xpath='/html/body/div[1]/section/section/main/div/div/div/div[2]/div/div/div[2]/div[1]/div/div/div[2]/form/div[3]/div[2]/div/div[2]/div/span/a')
    hu_ji_di_xiang_xi = PageElement(xpath='/html/body/div[1]/section/section/main/div/div/div/div[2]/div/div/div[2]/div[1]/div/div/div[2]/form/div[3]/div[3]/div/div/div/span/input')
    bei_jin_shi = PageElement(xpath='/html/body/div[3]/div/div/div/ul[1]/li[1]')
    dong_cheng_qu =PageElement(xpath='/html/body/div[3]/div/div/div/ul[2]/li[1]')
    kong_bai1 = PageElement(xpath='/html/body/div[1]/section/section/main/div/div/div/div[2]/div/div/div[2]/div[1]/div/div/div[2]/form/div[4]/div[1]')
    #居住地修改按钮和详细地址
    ju_zhu_di = PageElement(xpath='/html/body/div[1]/section/section/main/div/div/div/div[2]/div/div/div[2]/div[1]/div/div/div[2]/form/div[4]/div[2]/div/div[2]/div/span/a')
    ju_zhu_di_xiang_xi = PageElement(xpath='/html/body/div[1]/section/section/main/div/div/div/div[2]/div/div/div[2]/div[1]/div/div/div[2]/form/div[4]/div[3]/div/div/div/span/span/input')
    xi_zang_zi_zi_qu =PageElement(xpath='/html/body/div[4]/div/div/div/ul/li')
    chang_du_shi = PageElement(xpath='/html/body/div[4]/div/div/div/ul[2]/li')
    ka_ruo_qu = PageElement(xpath='/html/body/div[4]/div/div/div/ul[3]/li')
    ka_ruo_zheng = PageElement(xpath='/html/body/div[4]/div/div/div/ul[4]/li')
    ka_ruo_zheng_cuo_ming_wei_yuan_hui = PageElement(xpath='/html/body/div[4]/div/div/div/ul[5]/li')
    #完成建档按钮及断言元素
    wan_cheng_jian_dang = PageElement(xpath='/html/body/div[1]/section/section/main/div/div/div/div[2]/div/div/div[2]/div[1]/div/div/div[2]/form/div[5]/div/button[2]')
    da_yin_dang_an = PageElement(xpath='/html/body/div[1]/section/section/main/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/button[2]')
    fan_hui_lie_biao = PageElement(xpath='/html/body/div[1]/section/section/main/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/button[1]')


