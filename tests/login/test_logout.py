from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.home_page import HomePage
from pages.login_page import LoginPage
import test_data

def test_logout(driver):
    '''
    Test Case 4: Logout User
    '''

    home_page = HomePage(driver)
    home_page.open()

    homepage_title = home_page.get_title()

    assert test_data.BASE_URL in driver.current_url, f"Expected URL: '{test_data.BASE_URL}', actual URL: '{driver.current_url}'"
    assert homepage_title == test_data.HOMEPAGE_TITLE, f"Expected H1 text: '{test_data.HOMEPAGE_TITLE}', actual H1 text: '{homepage_title}'"

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

    WebDriverWait(driver, 5).until(EC.url_contains(test_data.LOGIN_PAGE_PATH))

    assert test_data.LOGIN_PAGE_PATH in driver.current_url, f"Expected URL: '{test_data.LOGIN_PAGE_PATH}', actual URL: '{driver.current_url}'"