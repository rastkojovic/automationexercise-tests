from selenium.webdriver.common.by import By
from pages.home_page import HomePage
from pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import test_data

def test_invalid_login(driver):
    
    home_page = HomePage(driver)
    home_page.open()

    WebDriverWait(driver, 5).until(expected_conditions.url_contains(test_data.BASE_URL))

    current_url = driver.current_url
    h1_text = driver.find_element(By.TAG_NAME, "h1").text

    assert test_data.BASE_URL in current_url, f"Expected URL: '{test_data.BASE_URL}', actual URL: '{current_url}'"
    assert h1_text == test_data.HOMEPAGE_H1_TEXT, f"Expected H1 text: '{test_data.HOMEPAGE_H1_TEXT}', actual H1 text: '{h1_text}'"

    home_page.click_signup_login()

    WebDriverWait(driver, 5).until(expected_conditions.url_contains(test_data.LOGIN_PAGE_PATH))

    login_form_title = driver.find_element(By.CSS_SELECTOR, ".login-form h2").text

    assert login_form_title == test_data.LOGIN_FORM_TITLE, f"Expected H2 text: '{test_data.LOGIN_FORM_TITLE}', actual H2 text: '{login_form_title}'"

    login_page = LoginPage(driver)
    login_page.enter_email(test_data.INVALID_EMAIL)
    login_page.enter_password(test_data.INVALID_PASSWORD)
    login_page.click_login_button()

    invalid_cred_msg = driver.find_element(By.CSS_SELECTOR, ".login-form p").text

    assert invalid_cred_msg == test_data.INVALID_CRED_MSG, f"Expected message: '{test_data.INVALID_CRED_MSG}', actual message: '{invalid_cred_msg}'"