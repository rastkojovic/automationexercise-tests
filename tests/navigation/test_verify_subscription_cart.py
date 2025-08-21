from pages.home_page import HomePage
from pages.cart_page import CartPage
import test_data

def test_verify_subscription_cart(driver):
    '''
    Test Case 11: Verify Subscription in Cart page
    '''

    home_page = HomePage(driver)
    home_page.open()

    homepage_title = home_page.get_title()

    assert test_data.BASE_URL in driver.current_url, f"Expected URL to contain {test_data.BASE_URL}, but got {driver.current_url}"
    assert test_data.HOMEPAGE_TITLE == homepage_title, f"Expected H1 text: {test_data.HOMEPAGE_TITLE}, actual H1 text: {homepage_title}"

    home_page.nav.click_cart()

    cart_page = CartPage(driver)
    cart_page.enter_subscription_email(test_data.EMAIL)
    cart_page.click_subscribe()

    success_message = cart_page.get_subscription_success_message()

    assert test_data.SUBSCRIPTION_SUCCESS_MESSAGE in success_message, f"Expected message: '{test_data.SUBSCRIPTION_SUCCESS_MESSAGE}', actual message: '{success_message}'"