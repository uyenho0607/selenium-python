import pytest

from Config.Config import DATA_TEST
from Pages.LoginPage import LoginPage
from Tests.test_Base import BaseTest


class Test_Login_Page(BaseTest):

    def test_verify_page_title(self):
        self.loginPage = LoginPage(self.driver)
        login_page_title = self.loginPage.get_page_title(DATA_TEST.LOGIN_PAGE_TITLE)
        assert login_page_title == DATA_TEST.LOGIN_PAGE_TITLE, "Verify page title failed"

    def test_do_login(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(DATA_TEST.USERNAME, DATA_TEST.PASSWORD)




