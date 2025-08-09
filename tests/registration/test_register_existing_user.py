import test_data
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from pages.home_page import HomePage
from pages.signup_page import SignupPage

def test_register_existing_user(driver):

    home_page = HomePage(driver)
    home_page.open()

    WebDriverWait(driver, 5).until(expected_conditions.url_contains(test_data.BASE_URL))

    current_url = driver.current_url
    homepage_h1_text = driver.find_element(By.TAG_NAME, "h1").text

    assert test_data.BASE_URL in current_url, f"Expected URL: '{test_data.BASE_URL}', actual URL: '{current_url}'"
    assert homepage_h1_text == test_data.HOMEPAGE_H1_TEXT, f"Expected H1 text: '{test_data.HOMEPAGE_H1_TEXT}', actual H1 text: '{homepage_h1_text}'"

    home_page.click_signup_login()

    WebDriverWait(driver, 5).until(expected_conditions.url_contains(test_data.LOGIN_PAGE_PATH))

    signup_page = SignupPage(driver)
    signup_form_title = signup_page.get_form_title()

    assert signup_form_title == test_data.SIGNUP_FORM_TITLE, f"Expected H2 text: '{test_data.SIGNUP_FORM_TITLE}', actual H2 text: '{signup_form_title}'"

    signup_page.enter_name(test_data.NAME)
    signup_page.enter_email(test_data.EMAIL)
    signup_page.click_signup_button()
    signup_error_msg = signup_page.get_error_msg()
    
    assert signup_error_msg == test_data.EXISTING_EMAIL_MSG, f"Expected error message: '{test_data.EXISTING_EMAIL_MSG}', actual error message: '{signup_error_msg}'"