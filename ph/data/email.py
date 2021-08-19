'''
发送邮件的发件人、收件人、邮件标题
邮件标题可以修改，不用的直接注释掉
'''
class email():
    mail_server = "smtp.qq.com"#邮箱地址
    send_user = "@qq.com"#发件人
    to_user = '@qq.com'#收件人
    # subject = 'web自动化测试报告测试报告' #邮件标题
    password = ""
    subject = '自动化测试报告' #邮件标题
