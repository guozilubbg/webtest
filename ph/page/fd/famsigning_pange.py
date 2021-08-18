'''
家庭签约页面
'''
from ph.common.PageObject import PageObject, PageElement
from ph.data.config import *
from ph.data.BaseData import *


class FamSigning_Page(PageObject):
    # 当前测试页面的测试网址url，目前操作是基于登录后的操作
    # base_url = Url.public_health_url
    # url = base_url + '/'

    #点击签约
    fam_famsigning_click = PageElement(xpath='//*[@id="app"]/section/section/main/div/div/div/div[2]/div/div/div/div[1]/div[1]/div/div[1]/button')

    # 选择服务类型
    #切近表单
    '''
    写个方法判断div+1
    '''
    fam_sig_form = PageElement(class_name='thick-form ant-form ant-form-horizontal')
    fam_sigtype_click = PageElement(xpath='//*[@id="signType"]/div')
    fam_sigtype1 = PageElement(xpath='/html/body/div[4]//*[@class="ant-select-dropdown-menu-item ant-select-dropdown-menu-item-active"]')
    fam_sigtype2 = PageElement(xpath='//*[@class="ant-select-dropdown ant-select-dropdown--single ant-select-dropdown-placement-bottomLeft"]/div/ul/li[2]')

    # 签发机构
    fam_signong = PageElement(xpath='//*[@id="signOrg"]/div')
    fam_sigadd1 = PageElement(xpath='/html/body/div[5]//*[@class="ant-select-dropdown-menu-item ant-select-dropdown-menu-item-active"]')

    # 服务团队
    fam_sigteam = PageElement(xpath='//*[@id="serviceTeamCode"]/div/div')
    fam_sigteam1 = PageElement(xpath='//li[contains(text(), "团队162")]')
    #调试
    a = BaseData.team_name
    xpath1 = '//li[contains(text(), "%s")]'%str(a.strip())
    print(xpath1)
    fam_sigteam2 = PageElement(xpath=xpath1)


    # 签约服务家庭
    fam_fam = PageElement(xpath='//*[@id="app"]/section/section/main/div/div/div/div[2]/div/div/form/div[2]/div[1]/div/div/span/span/input')
    fam_fam_clck = PageElement(xpath='//*[@id="app"]/section/section/main/div/div/div/div[2]/div/div/form/div[2]/div[1]/div/div/span/span/span')

    # 签约服务包
    fam_servicePackCode_click = PageElement(xpath='//*[@id="servicePackCode"]')
    fam_servicePackCode1 = PageElement(xpath='//li[contains(text(), "测试包162")]')


    # 保存
    fam_save = PageElement(xpath='//*[@id="app"]/section/section/main/div/div/div/div[2]/div/div/form/div[4]/div/button[1]')
    fam_save_goon = PageElement(xpath='//*[@class="ant-modal-confirm-body-wrapper"]/div[2]/button[2]')

if __name__ =='__main__':
    print(BaseData.team_name)