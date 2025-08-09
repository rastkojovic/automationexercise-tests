from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from pages.home_page import HomePage
import test_data

def test_verify_subscription_home(driver):
    
    home_page = HomePage(driver)   
    home_page.open()

    WebDriverWait(driver, 5).until(expected_conditions.url_contains(test_data.BASE_URL))

    current_url = driver.current_url
    home_page_h1_text = home_page.get_h1_text()

    assert test_data.BASE_URL in current_url, f"Expected URL: '{test_data.BASE_URL}', actual URL: '{current_url}'"
    assert home_page_h1_text == test_data.HOMEPAGE_H1_TEXT, f"Expected H1 text: {test_data.HOMEPAGE_H1_TEXT}, actual H1 text: {home_page_h1_text}"

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    home_page.enter_subscription_email(test_data.EMAIL)
    home_page.click_subscribe()

    subscription_message = home_page.get_subscription_success_message()
    assert test_data.SUBSCRIPTION_SUCCESS_MESSAGE in subscription_message, f"Expected message: '{test_data.SUBSCRIPTION_SUCCESS_MESSAGE}', actual message: '{subscription_message}'"