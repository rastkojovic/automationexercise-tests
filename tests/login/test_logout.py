from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
import test_data

def test_logout(driver, home_page, ensure_account):
    '''
    Test Case 4: Logout User
    '''

    home_page.nav.click_signup_login()

    login_page = LoginPage(driver)
    login_form_title = login_page.get_login_form_title()
    assert login_form_title == test_data.LOGIN_FORM_TITLE, f"Expected H2 text: '{test_data.LOGIN_FORM_TITLE}', actual H2 text: '{login_form_title}'"

    login_page.enter_email(test_data.EMAIL)
    login_page.enter_password(test_data.PASSWORD)
    login_page.click_login_button()

    logged_in_msg = home_page.nav.get_loggedin_msg()
    assert test_data.LOGGED_IN_MSG in logged_in_msg, f"Expected link text to contain: '{test_data.LOGGED_IN_MSG}', actual link text: '{logged_in_msg}'"

    home_page.nav.click_logout()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.url_contains(test_data.LOGIN_PAGE_PATH))
    assert test_data.LOGIN_PAGE_PATH in driver.current_url, f"Expected URL: '{test_data.LOGIN_PAGE_PATH}', actual URL: '{driver.current_url}'"