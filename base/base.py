'''
主要重新封装了一些方法，比如抓元素，等待
'''

from telnetlib import EC
from selenium import webdriver
from selenium.webdriver.support.expected_conditions import NoSuchElementException
import time as t

from selenium.webdriver.support.wait import WebDriverWait


class WebDriver(object):
    def __init__(self, driver):
        driver = webdriver.Firefox()
        self.driver = driver

    # def findElement(self,*loc):
    # 	try:
    # 		return self.driver.find_element(*loc)
    # 	except  NoSuchElementException as e:
    # 		print ('Error details :%s' % (e.args[0]))

    def wait(self):
        t.sleep(2)

    def refersh(self):
        self.driver.refresh()

    # 重写元素定位方法

    def find_element(self, *loc):
        #        return self.driver.find_element(*loc)
        try:
            # 确保元素是可见的。
            # 注意：以下入参为元组的元素，需要加*。Python存在这种特性，就是将入参放在元组里。
            #            WebDriverWait(self.driver,10).until(lambda driver: driver.find_element(*loc).is_displayed())
            # 注意：以下入参本身是元组，不需要加*
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except:
            print("%s 页面中未能找到 %s 元素" % (self, loc))

    # 重写switch_frame方法
    def switch_frame(self, loc):
        return self.driver.switch_to_frame(loc)

    # 定义script方法，用于执行js脚本，范围执行结果
    def script(self, src):
        self.driver.execute_script(src)

    # 重写定义send_keys方法
    def send_keys(self, loc, vaule, clear_first=True, click_first=True):
        try:
            loc = getattr(self, "_%s" % loc)  # getattr相当于实现self.loc
            if click_first:
                self.find_element(*loc).click()
            if clear_first:
                self.find_element(*loc).clear()
                self.find_element(*loc).send_keys(vaule)
        except AttributeError:
            print("%s 页面中未能找到 %s 元素" % (self, loc))
