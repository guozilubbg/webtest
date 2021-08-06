import os
import time
# 用例失败截图存放地址
ROOT = os.path.dirname(os.path.realpath(__file__))
pic_path = os.path.join(os.path.dirname(ROOT), 'pic')
# 如果不存在这个logs文件夹，就自动创建一个
if not os.path.exists(pic_path): os.mkdir(pic_path)


# class Screenshot():


def screenshot_image1(webdriver, image_path):
    nowTime = time.strftime("%Y-%m-%d_%H-%M-%S")
    imageName = image_path + "/" + "bug_image{}.png".format(nowTime)
    webdriver.save_screenshot(imageName)

def screenshot_image2(webdriver, image_path):
    nowTime = time.strftime("%Y-%m-%d_%H-%M-%S")
    imageName = image_path + "/" + "bug_image{}.png".format(nowTime)
    webdriver.get_screenshot_as_file(imageName)
