'''
封装一些基本函数
'''
from selenium import webdriver
from selenium.webdriver.common.by import By

_LOCATOR_MAP = {'css': By.CSS_SELECTOR,
                'id': By.ID,
                'name': By.NAME,
                'xpath': By.XPATH,
                'link_text': By.LINK_TEXT,
                'partial_link_text': By.PARTIAL_LINK_TEXT,
                'tag_name': By.TAG_NAME,
                'class_name': By.CLASS_NAME,
                }


class Base:

    def __init__(self,driver):
        self.driver = driver

    def visit(self, url):
        self.driver.get(url)

    def find(self, loc):
        # k, v = next(iter(loc.items()))
        # locator = (_LOCATOR_MAP[k], v)
        return self.driver.find_element(*loc)

    def input(self, loc, value):
        self.find(loc).send_keys(value)

    def click(self, loc):
        self.find(loc).click()
