import test_data

def test_verify_subscription_home(driver, home_page):
    '''
    Test Case 10: Verify Subscription in home page
    '''

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    home_page.enter_subscription_email(test_data.EMAIL)
    home_page.click_subscribe()

    subscription_message = home_page.get_subscription_success_message()
    assert test_data.SUBSCRIPTION_SUCCESS_MESSAGE in subscription_message, f"Expected message: '{test_data.SUBSCRIPTION_SUCCESS_MESSAGE}', actual message: '{subscription_message}'"