from testcase.ph.login.test_login import Testlogin


class BaseHandle():
    def login(self):
        Testlogin().setUp()
        Testlogin().test_login()



