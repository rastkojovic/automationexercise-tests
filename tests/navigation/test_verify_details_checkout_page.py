from flows.account_flow import AccountFlow
from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
import test_data

def test_verify_details_checkout_page(driver, home_page):
    '''
    Test Case 23: Verify address details in checkout page
    '''

    home_page.nav.click_signup_login()
    account_flow = AccountFlow(driver)
    login_page = LoginPage(driver)
    signup_page = SignupPage(driver)

    # Create account [Example using AccountFlow]
    account_flow.create(login_page, signup_page)

    # Verify login
    logged_in_msg = home_page.nav.get_loggedin_msg()
    assert logged_in_msg in test_data.LOGGED_IN_MSG, f"Expected message: '{test_data.LOGGED_IN_MSG}', actual message: '{logged_in_msg}'"

    # Add products to cart
    home_page.add_to_cart(2)
    home_page.add_to_cart(5)
    home_page.add_to_cart(7)

    # Click cart button
    home_page.nav.click_cart()

    # Proceed to checkout
    cart_page = CartPage(driver)
    cart_page.click_checkout_button()

    # Verify that the delivery address is same address filled at the time registration of account
    checkout_page = CheckoutPage(driver)
    address_details = checkout_page.get_address_details()
    set_address1 = address_details["address_1"]
    set_address2 = address_details["address_2"]

    assert test_data.ADDRESS1 in set_address1, f"Expected address1 to be: '{test_data.ADDRESS1}', actual address: '{set_address1}'"
    assert test_data.ADDRESS2 in set_address2, f"Expected address1 to be: '{test_data.ADDRESS2}', actual address: '{set_address2}'"

    # Click 'Delete Account' button
    account_flow.delete(checkout_page)
