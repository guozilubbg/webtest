'''
获取测试用例并且发送邮件
'''
import HTMLTestRunner
import time
import unittest
from common.sendEmail import SendEmail


class GenerateTestReport:
    def get_test_cases(dirpath=None):
        # dirpath是存放测试用例的文件路径
        dirpath = str(dirpath)
        test_cases = unittest.TestSuite()
        # 测试用例均使用"test_"开头命名
        suites = unittest.defaultTestLoader.discover(dirpath, 'test_*.py', top_level_dir=dirpath)
        for suite in suites:
            test_cases.addTests(suite)
        return test_cases
    def generate_report(dirpath=None):#传参为用例路径
        cases = GenerateTestReport.get_test_cases(dirpath)
        now = time.strftime("%Y-%m-%d %H_%M_%S")  # 报告生成时间
        test_reports_address = './report'  # 测试报告存放位置
        filename = './report/' + now + 'report.html'  # 设置报告文件名
        fp = open(filename, 'wb')
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'Web自动化测试', description=u'详细测试结果如下:')
        runner.run(cases)
        fp.close()
        # 向指定邮箱发送测试报告的html文件
        time.sleep(6)
        # 查找最新生成的测试报告地址
        new_report_addr = SendEmail().acquire_report_address(test_reports_address)
        # 自动发送邮件
        # SendEmail().send_email(new_report_addr)
