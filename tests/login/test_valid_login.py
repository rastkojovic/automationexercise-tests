from pages.home_page import HomePage
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import test_data

def test_valid_login(driver):
    
    home_page = HomePage(driver)
    home_page.open()

    WebDriverWait(driver, 5).until(expected_conditions.url_contains(test_data.BASE_URL))

    current_url = driver.current_url
    homepage_h1_text = driver.find_element(By.TAG_NAME, "h1").text

    assert test_data.BASE_URL in current_url, f"Expected URL: '{test_data.BASE_URL}', actual URL: '{current_url}'"
    assert homepage_h1_text == test_data.HOMEPAGE_H1_TEXT, f"Expected H1 text: {test_data.HOMEPAGE_H1_TEXT}, actual H1 text: {homepage_h1_text}"

    home_page.click_signup_login()

    login_form_title = driver.find_element(By.CSS_SELECTOR, "#form .login-form h2").text

    assert login_form_title == test_data.LOGIN_FORM_TITLE, f"Expected H2 text: '{test_data.LOGIN_FORM_TITLE}', actual H2 text: '{login_form_title}'"

    login_page = LoginPage(driver)
    login_page.enter_email(test_data.EMAIL)
    login_page.enter_password(test_data.PASSWORD)
    login_page.click_login_button()

    WebDriverWait(driver, 5).until(expected_conditions.url_contains(test_data.BASE_URL))

    navbar_items = driver.find_elements(By.CSS_SELECTOR, ".navbar-nav li")
    logged_in_text = navbar_items[9].text.strip()

    assert logged_in_text == f"Logged in as {test_data.NAME}", f"Expected text: 'Logged in as {test_data.NAME}', actual text: '{logged_in_text}'"

    home_page.delete_account()

    account_deleted_title = driver.find_element(By.CSS_SELECTOR, "h2[data-qa='account-deleted']").text

    assert account_deleted_title == test_data.ACCOUNT_DELETED_TITLE, f"Expected H2 text: '{test_data.ACCOUNT_DELETED_TITLE}', actual H2 text: '{account_deleted_title}'"