from pages.home_page import HomePage
import test_data

def test_testcases(driver):

    home_page = HomePage(driver)
    home_page.open()

    current_url = driver.current_url
    homepage_title = home_page.get_title()

    assert test_data.BASE_URL in current_url, f"Expected URL: '{test_data.BASE_URL}', actual URL: '{current_url}'"
    assert homepage_title == test_data.HOMEPAGE_TITLE, f"Expected H1 text: '{test_data.HOMEPAGE_TITLE}', actual H1 text: '{homepage_title}'"

    home_page.nav.click_testcases()

    current_url = driver.current_url
    assert test_data.TEST_CASES_PAGE_PATH in current_url, f"Expected URL: '{test_data.TEST_CASES_PAGE_PATH}', actual URL: '{current_url}'"