from pages.home_page import HomePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import test_data

def test_testcases(driver):

    home_page = HomePage(driver)
    home_page.open()

    WebDriverWait(driver, 5).until(expected_conditions.url_contains(test_data.BASE_URL))

    current_url = driver.current_url
    homepage_h1_text = home_page.get_h1_text()

    assert test_data.BASE_URL in current_url, f"Expected URL: '{test_data.BASE_URL}', actual URL: '{current_url}'"
    assert homepage_h1_text == test_data.HOMEPAGE_H1_TEXT, f"Expected H1 text: '{test_data.HOMEPAGE_H1_TEXT}', actual H1 text: '{homepage_h1_text}'"

    home_page.click_testcases()

    WebDriverWait(driver, 5).until(expected_conditions.url_contains(test_data.TEST_CASES_PAGE_PATH))

    current_url = driver.current_url
    assert test_data.TEST_CASES_PAGE_PATH in current_url, f"Expected URL: '{test_data.TEST_CASES_PAGE_PATH}', actual URL: '{current_url}'"