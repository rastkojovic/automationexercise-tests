import test_data
from pages.signup_page import SignupPage

def test_register_existing_user(driver, home_page):
    '''
    Test Case 5: Register User with existing email
    '''

    home_page.nav.click_signup_login()

    signup_page = SignupPage(driver)
    signup_form_title = signup_page.get_form_title()

    assert signup_form_title == test_data.SIGNUP_FORM_TITLE, f"Expected H2 text: '{test_data.SIGNUP_FORM_TITLE}', actual H2 text: '{signup_form_title}'"

    signup_page.enter_name(test_data.NAME)
    signup_page.enter_email(test_data.EMAIL)
    signup_page.click_signup_button()
    signup_error_msg = signup_page.get_error_msg()
    
    assert signup_error_msg == test_data.EXISTING_EMAIL_MSG, f"Expected error message: '{test_data.EXISTING_EMAIL_MSG}', actual error message: '{signup_error_msg}'"