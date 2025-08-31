import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException
from flows.account_flow import AccountFlow

@pytest.fixture
def driver():
    options = Options()
    options.add_argument('--incognito')
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

@pytest.fixture
def home_page(driver):
    page = HomePage(driver)
    page.open()
    page.assert_is_open()
    return page

@pytest.fixture
def ensure_account(driver, home_page):

    flow = AccountFlow(driver)

    # Setup: Create account
    home_page.nav.click_signup_login()
    login_page = LoginPage(driver)
    signup_page = SignupPage(driver)
    flow.create(login_page, signup_page)
    flow.logout(home_page)

    yield

    # Teardown: Delete account
    try:
        flow.delete(login_page)
    except (NoSuchElementException, TimeoutException, StaleElementReferenceException):
        flow.login(login_page)
        flow.delete(login_page)
    