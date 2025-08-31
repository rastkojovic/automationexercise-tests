from pages.login_page import LoginPage
import test_data

def test_invalid_login(driver, home_page):
    '''
    Test Case 3: Login User with incorrect email and password
    '''

    home_page.nav.click_signup_login()

    login_page = LoginPage(driver)
    login_form_title = login_page.get_login_form_title()
    assert login_form_title == test_data.LOGIN_FORM_TITLE, f"Expected H2 text: '{test_data.LOGIN_FORM_TITLE}', actual H2 text: '{login_form_title}'"

    login_page.enter_email(test_data.INVALID_EMAIL)
    login_page.enter_password(test_data.INVALID_PASSWORD)
    login_page.click_login_button()

    invalid_cred_msg = login_page.get_invalid_cred_msg()
    assert invalid_cred_msg == test_data.INVALID_CRED_MSG, f"Expected message: '{test_data.INVALID_CRED_MSG}', actual message: '{invalid_cred_msg}'"