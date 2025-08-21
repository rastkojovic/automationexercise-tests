from pages.home_page import HomePage
import test_data

def test_verify_subscription_home(driver):
    '''
    Test Case 10: Verify Subscription in home page
    '''
    
    home_page = HomePage(driver)   
    home_page.open()

    homepage_title = home_page.get_title()

    assert test_data.BASE_URL in driver.current_url, f"Expected URL: '{test_data.BASE_URL}', actual URL: '{driver.current_url}'"
    assert homepage_title == test_data.HOMEPAGE_TITLE, f"Expected H1 text: {test_data.HOMEPAGE_TITLE}, actual H1 text: {homepage_title}"

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    home_page.enter_subscription_email(test_data.EMAIL)
    home_page.click_subscribe()

    subscription_message = home_page.get_subscription_success_message()
    assert test_data.SUBSCRIPTION_SUCCESS_MESSAGE in subscription_message, f"Expected message: '{test_data.SUBSCRIPTION_SUCCESS_MESSAGE}', actual message: '{subscription_message}'"