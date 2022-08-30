from selenium.webdriver.common.by import By

from Config.Config import DATA_TEST
from Pages.BasePage import BasePage


class LoginPage(BasePage):

    """Page Constructor"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(DATA_TEST.base_url)

    """Page Locators"""

    EMAIL_TB = (By.ID, 'username')
    PASSWORD_TB = (By.ID, 'password')
    LOGIN_BTN = (By.ID, 'loginBtn')

    """Page Methods"""
    def get_login_page_title(self, title):
        return self.get_page_title(title)

    def do_login(self, username, password):
        self.do_clear(self.EMAIL_TB)
        self.do_send_keys(self.EMAIL_TB, username)
        self.do_clear(self.PASSWORD_TB)
        self.do_send_keys(self.PASSWORD_TB, password)
        self.do_click(self.LOGIN_BTN)



