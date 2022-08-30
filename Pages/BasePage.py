from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def do_click(self, by_locator):
        self.wait.until(ec.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        self.wait.until(ec.visibility_of_element_located(by_locator)).send_keys(text)

    def do_clear(self, by_locator):
        self.wait.until(ec.visibility_of_element_located(by_locator)).clear()

    def get_page_title(self, title):
        self.wait.until(ec.title_is(title))
        return self.driver.title


