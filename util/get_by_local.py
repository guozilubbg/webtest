from util.read_init import ReadIni
from selenium import webdriver


class GetByLocal:
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, key):
        read_ini = ReadIni()
        local = read_ini.get_value(key)
        if local != None:
            by = local.split('>')[0]
            local_by = local.split('>')[1]
            try:
                if by == 'id':
                    return self.driver.find_element_by_id(local_by)
                elif by == 'className':
                    return self.driver.find_element_by_class_name(local_by)
                elif by == 'name':
                    return self.driver.find_element_by_name(local_by)
                else:
                    return self.driver.find_element_by_xpath(local_by)
            except:
                # self.driver.save_screenshot("../jpg/test02.png")
                return None
        else:
            return None


if __name__ == '__main__':
    read_ini = ReadIni()
    print(read_ini.get_value("paizhao", "login_element"))
    print(read_ini.get_value("baidu", "login_element"))
    print(GetByLocal.get_element("paizhao", "login_element"))
    print(GetByLocal.get_element("baidu", "login_element"))
