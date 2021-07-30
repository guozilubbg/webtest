from common.pageObject import PageObject, PageElement
from data.url import *


class familydocter(PageObject):
    # 当前测试页面的测试网址url
    base_url = Url.public_health_url
    url = base_url + '/'

    # 定位到家医签约
    fam_doc = PageElement(text="全民健康体检")
