'''
家庭档案管理
'''
from ph.common.PageObject import PageObject, PageElement
from ph.data.config import *
class AddJtda(PageObject):
    #健康档案导航按钮
    jkda_dh = PageElement(xpath='/html/body/div[1]/section/section/header/div/div/div[2]/ul/li[4]/div/span/span/span')
    #家庭档案导航按钮
    jia_ting_dang_an = PageElement(xpath='/html/body/div[2]/div/div/ul/li[3]/a')
    #新增家庭档案按钮
    xin_zeng_jia_ting_dang_an = PageElement(xpath='/html/body/div[1]/section/section/main/div/div/div/div[2]/div/div/div[1]/div[1]/div/div[1]/button')
    #家庭档案身份证号码输入框
    jt_shen_fen_zheng_hao = PageElement(xpath='/html/body/div[1]/section/section/main/div/div/div/div[2]/div/div/div/div[2]/div[1]/div/form/div[1]/div[1]/div/div[2]/div/span/span/input')
    # 家庭-读卡按钮
    jt_du_ka = PageElement(xpath='/html/body/div[1]/section/section/main/div/div/div/div[2]/div/div/div/div[2]/div[1]/div/form/div[1]/div[1]/div/div[2]/div/span/span/button')
    # 家庭-责任医生框
    ze_ren_yi_sheng = PageElement(xpath='/html/body/div[1]/section/section/main/div/div/div/div[2]/div/div/div/div[2]/div[1]/div/form/div[3]/div[2]/div/div[2]/div/span/div/div/div')
    yi_sheng_div = PageElement(xpath='/html/body/div[8]/div/div/div')
    yi_sheng_xing_ming = PageElement(xpath="//li[contions(text(),'西绕卡珠')]")
    # 下一步管理家庭成员
    xia_yi_bu = PageElement(xpath='//*[@id="app"]/section/section/main/div/div/div/div[2]/div/div/div/div[2]/div[1]/div/form/div[5]/div/button[1]')
    # 添加家庭成员
    tian_jia_jia_ting_cheng_yuan = PageElement(xpath='/html/body/div[1]/section/section/main/div/div/div/div[2]/div/div/div/div[2]/div[2]/form/div[1]/button')
    #进入from
    from1 = PageElement(xpath='/html/body/div[4]/div/div[2]/div/div[2]/div[2]/div/div/form')
    # 家庭成员身份证号
    jia_ting_cheng_yuan_sheng_fen_zheng_hao_xpath = PageElement(xpath='/html/body/div[4]/div/div[2]/div/div[2]/div[2]/div/div/form/div[3]/div[2]/div/span/input')
    jia_ting_cheng_yuan_sheng_fen_zheng_hao_id = PageElement(xpath="//span[contains(id(),'zjhm']")
    # 姓名
    xing_ming = PageElement(xpath='/html/body/div[4]/div/div[2]/div/div[2]/div[2]/div/div/form/div[1]/div[2]/div/span/input')
    # 户主关系下拉框
    yu_hu_zhu_guan_xi = PageElement(xpath='/html/body/div[4]/div/div[2]/div/div[2]/div[2]/div/div/form/div[2]/div[2]/div/span/div/div/div')
    # 选择配偶
    pei_ou = PageElement(xpath="//li[contains(text(),'配偶')]")
    # 点击确认按钮
    jt_que_ren = PageElement(xpath='/html/body/div[4]/div/div[2]/div/div[2]/div[3]/div/button[2]')
    # 点击完成按钮
    jt_wan_cheng = PageElement(xpath='/html/body/div[1]/section/section/main/div/div/div/div[2]/div/div/div/div[2]/div[2]/form/div[3]/div/button[2]')
