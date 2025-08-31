from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from pages.checkout_page import CheckoutPage
from pages.payment_page import PaymentPage
from flows.account_flow import AccountFlow
import test_data

def test_register_while_checkout(driver, home_page):
    '''
    Test Case 14: Place Order: Register while Checkout
    '''

    # ADD ITEMS TO CART
    product_page = ProductPage(driver)
    product_page.add_to_cart(2)
    product_page.dialogue.continue_shopping()
    product_page.add_to_cart(4)
    product_page.dialogue.continue_shopping()
    product_page.add_to_cart(6)
    product_page.dialogue.continue_shopping()
    home_page.nav.click_cart()

    assert test_data.CART_PAGE_PATH in driver.current_url, f"Expected page: {test_data.CART_PAGE_PATH}, actual page: {driver.current_url}"

    cart_page = CartPage(driver)
    cart_page.click_checkout_button()

    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".modal-body a[href='/login']")))
    cart_page.click_register_login_link()

    wait.until(EC.url_contains(test_data.LOGIN_PAGE_PATH))

    # REGISTER NEW USER
    flow = AccountFlow(driver)
    login_page = LoginPage(driver)
    signup_page = SignupPage(driver)
    flow.create(login_page, signup_page)

    # PROCEED WITH CHECKOUT
    home_page.nav.click_cart()
    assert test_data.CART_PAGE_PATH in driver.current_url, f"Expected page: {test_data.CART_PAGE_PATH}, actual page: {driver.current_url}"

    cart_page.click_checkout_button()

    # VERIFY DETAILS
    checkout_page = CheckoutPage(driver)
    address_details = checkout_page.get_address_details()

    assert test_data.TITLE == address_details["title"]
    assert test_data.NAME == address_details["first_name"]
    assert test_data.LAST_NAME == address_details["last_name"]
    assert test_data.COMPANY == address_details["company_name"]
    assert test_data.ADDRESS1 == address_details["address_1"]
    assert test_data.ADDRESS2 == address_details["address_2"]
    assert test_data.COUNTRY == address_details["country"]
    assert test_data.STATE == address_details["state"]
    assert test_data.CITY == address_details["city"]
    assert test_data.ZIP == address_details["post_code"]
    assert test_data.PHONE_NUM == address_details["phone_num"]

    checkout_page.enter_message("This is a comment on the order.")
    checkout_page.click_payment_btn()

    wait.until(EC.url_contains(test_data.PAYMENT_PAGE_PATH))

    # ENTER PAYMENT INFO & CONFIRM PURCHASE
    payment_page = PaymentPage(driver)
    payment_page.enter_card_name(f"{test_data.NAME} {test_data.LAST_NAME}")
    payment_page.enter_card_num(test_data.CARD_NUMBER)
    payment_page.enter_cvc(test_data.CVC)
    payment_page.enter_expiry_month(test_data.EXPIRY_MONTH)
    payment_page.enter_expiry_year(test_data.EXPIRY_YEAR)
    # Any wait started after .click() (which blocks until navigation) will always miss the visible state and time out.
    # Prevent first submit
    driver.execute_script("""
  const f = document.getElementById('payment-form');
  if (f) f.addEventListener('submit', e => e.preventDefault(), { once: true });
""")
    payment_page.pay_and_confirm()
    assert payment_page.success_msg_present(), f"Expected success message: '{test_data.ORDER_SUCCESS_MESSAGE}' but got none"
    payment_page.pay_and_confirm()
    wait.until(EC.url_contains("payment_done"))

    # Delete account
    flow.delete(payment_page)