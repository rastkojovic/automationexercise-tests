from selenium.webdriver.common.by import By
from pages.home_page import HomePage
from pages.login_page import LoginPage
import test_data

def test_invalid_login(driver):
    
    home_page = HomePage(driver)
    home_page.open()

    current_url = driver.current_url
    h1_text = driver.find_element(By.TAG_NAME, "h1").text

    assert current_url == test_data.HOMEPAGE_URL, f"Expected URL: '{test_data.HOMEPAGE_URL}', actual URL: '{current_url}'"
    assert h1_text == test_data.HOMEPAGE_H1_TEXT, f"Expected H1 text: '{test_data.HOMEPAGE_H1_TEXT}', actual H1 text: '{h1_text}'"

    home_page.click_signup_login()

    login_form_title = driver.find_element(By.CSS_SELECTOR, ".login-form h2").text

    assert login_form_title == test_data.LOGIN_FORM_TITLE, f"Expected H2 text: '{test_data.LOGIN_FORM_TITLE}', actual H2 text: '{login_form_title}'"

    login_page = LoginPage(driver)
    login_page.enter_email(test_data.INVALID_EMAIL)
    login_page.enter_password(test_data.INVALID_PASSWORD)
    login_page.click_login_button()

    invalid_cred_msg = driver.find_element(By.CSS_SELECTOR, ".login-form p").text

    assert invalid_cred_msg == test_data.INVALID_CRED_MSG, f"Expected message: '{test_data.INVALID_CRED_MSG}', actual message: '{invalid_cred_msg}'"