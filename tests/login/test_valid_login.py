from pages.login_page import LoginPage
from pages.delete_page import DeletePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import test_data

def test_valid_login(driver, home_page, ensure_account):
    '''
    Test Case 2: Login User with correct email and password
    '''

    home_page.nav.click_signup_login()

    login_page = LoginPage(driver)
    assert login_page.get_login_form_title() == test_data.LOGIN_FORM_TITLE, f"Expected H2 text: '{test_data.LOGIN_FORM_TITLE}', actual H2 text: '{login_page.get_login_form_title()}'"

    login_page.enter_email(test_data.EMAIL)
    login_page.enter_password(test_data.PASSWORD)
    login_page.click_login_button()

    wait = WebDriverWait(driver, 10)
    wait.until(EC.url_contains(test_data.BASE_URL))

    logged_in_text = home_page.nav.get_loggedin_msg()
    assert logged_in_text == f"Logged in as {test_data.NAME}", f"Expected text: 'Logged in as {test_data.NAME}', actual text: '{logged_in_text}'"