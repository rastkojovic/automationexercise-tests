from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
import test_data

def test_logout(driver, home_page):
    '''
    Test Case 4: Logout User
    '''

    home_page.nav.click_signup_login()

    login_page = LoginPage(driver)
    login_form_title = driver.find_element(By.CSS_SELECTOR, ".login-form h2").text

    assert login_form_title == test_data.LOGIN_FORM_TITLE, f"Expected H2 text: '{test_data.LOGIN_FORM_TITLE}', actual H2 text: '{login_form_title}'"

    login_page.enter_email(test_data.EMAIL)
    login_page.enter_password(test_data.PASSWORD)
    login_page.click_login_button()

    logged_in_msg = home_page.nav.get_loggedin_msg()
    assert logged_in_msg == test_data.LOGGED_IN_MSG, f"Expected message: '{test_data.LOGGED_IN_MSG}', actual message: '{logged_in_msg}'"

    home_page.logout()

    WebDriverWait(driver, 10).until(EC.url_contains(test_data.LOGIN_PAGE_PATH))

    assert test_data.LOGIN_PAGE_PATH in driver.current_url, f"Expected URL: '{test_data.LOGIN_PAGE_PATH}', actual URL: '{driver.current_url}'"