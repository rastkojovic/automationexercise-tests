import pytest
from pages.home_page import HomePage
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import test_data

@pytest.fixture
def driver():

    options = Options()
    options.add_argument('--incognito')
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

@pytest.fixture
def home_page(driver):
    page = HomePage(driver)
    page.open()
    page.assert_is_open()
    return page