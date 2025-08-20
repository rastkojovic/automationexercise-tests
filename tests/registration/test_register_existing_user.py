import test_data
from selenium.webdriver.common.by import By
from pages.home_page import HomePage
from pages.signup_page import SignupPage

def test_register_existing_user(driver):

    home_page = HomePage(driver)
    home_page.open()

    current_url = driver.current_url
    homepage_title = driver.find_element(By.TAG_NAME, "h1").text

    assert test_data.BASE_URL in current_url, f"Expected URL: '{test_data.BASE_URL}', actual URL: '{current_url}'"
    assert homepage_title == test_data.HOMEPAGE_TITLE, f"Expected H1 text: '{test_data.HOMEPAGE_TITLE}', actual H1 text: '{homepage_title}'"

    home_page.nav.click_signup_login()

    signup_page = SignupPage(driver)
    signup_form_title = signup_page.get_form_title()

    assert signup_form_title == test_data.SIGNUP_FORM_TITLE, f"Expected H2 text: '{test_data.SIGNUP_FORM_TITLE}', actual H2 text: '{signup_form_title}'"

    signup_page.enter_name(test_data.NAME)
    signup_page.enter_email(test_data.EMAIL)
    signup_page.click_signup_button()
    signup_error_msg = signup_page.get_error_msg()
    
    assert signup_error_msg == test_data.EXISTING_EMAIL_MSG, f"Expected error message: '{test_data.EXISTING_EMAIL_MSG}', actual error message: '{signup_error_msg}'"