import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from Config.Config import DATA_TEST


@pytest.fixture(params=['chrome', 'firefox'], scope='class')
def init_driver(request):
    if request.param == 'chrome':
        web_driver = webdriver.Chrome(executable_path=DATA_TEST.CHROME_PATH)
    if request.param == 'firefox':
        web_driver = webdriver.Firefox(executable_path=DATA_TEST.GECKO_PATH)
    request.cls.driver = web_driver
    yield
    web_driver.close()


@pytest.fixture
def chrome_options(chrome_options):
    chrome_options.add_argument('--headless')
    return chrome_options


@pytest.fixture
def firefox_options(firefox_options):
    firefox_options.add_argument('-headless')
    return firefox_options