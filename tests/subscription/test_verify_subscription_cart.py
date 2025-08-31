from pages.cart_page import CartPage
import test_data

def test_verify_subscription_cart(driver, home_page):
    '''
    Test Case 11: Verify Subscription in Cart page
    '''

    home_page.nav.click_cart()

    cart_page = CartPage(driver)
    cart_page.enter_subscription_email(test_data.EMAIL)
    cart_page.click_subscribe()

    success_message = cart_page.get_subscription_success_message()

    assert test_data.SUBSCRIPTION_SUCCESS_MESSAGE in success_message, f"Expected message: '{test_data.SUBSCRIPTION_SUCCESS_MESSAGE}', actual message: '{success_message}'"