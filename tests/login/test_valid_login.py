from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import test_data

def test_valid_login(driver, home_page):
    '''
    Test Case 2: Login User with correct email and password
    '''

    home_page.nav.click_signup_login()

    login_form_title = driver.find_element(By.CSS_SELECTOR, "#form .login-form h2").text

    assert login_form_title == test_data.LOGIN_FORM_TITLE, f"Expected H2 text: '{test_data.LOGIN_FORM_TITLE}', actual H2 text: '{login_form_title}'"

    login_page = LoginPage(driver)
    login_page.enter_email(test_data.EMAIL)
    login_page.enter_password(test_data.PASSWORD)
    login_page.click_login_button()

    WebDriverWait(driver, 10).until(EC.url_contains(test_data.BASE_URL))

    navbar_items = driver.find_elements(By.CSS_SELECTOR, ".navbar-nav li")
    logged_in_text = navbar_items[9].text.strip()

    assert logged_in_text == f"Logged in as {test_data.NAME}", f"Expected text: 'Logged in as {test_data.NAME}', actual text: '{logged_in_text}'"

    home_page.nav.click_delete_account()

    account_deleted_title = driver.find_element(By.CSS_SELECTOR, "h2[data-qa='account-deleted']").text

    assert account_deleted_title == test_data.ACCOUNT_DELETED_TITLE, f"Expected H2 text: '{test_data.ACCOUNT_DELETED_TITLE}', actual H2 text: '{account_deleted_title}'"