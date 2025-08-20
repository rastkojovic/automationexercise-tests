from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.payment_page import PaymentPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import test_data

def test_login_before_checkout(driver):

    home_page = HomePage(driver)
    home_page.open()

    current_url = driver.current_url
    homepage_title = driver.find_element(By.TAG_NAME, "h1").text

    assert test_data.BASE_URL in current_url, f"Expected URL: '{test_data.BASE_URL}', actual URL: '{current_url}'"
    assert test_data.HOMEPAGE_TITLE in homepage_title, f"Expected title: '{test_data.HOMEPAGE_TITLE}', actual title: '{homepage_title}'"

    home_page.nav.click_signup_login()

    wait = WebDriverWait(driver, 5)
    
    login_page = LoginPage(driver)
    login_page.enter_email(test_data.EMAIL)
    login_page.enter_password(test_data.PASSWORD)
    login_page.click_login_button()

    wait.until(EC.url_contains(test_data.BASE_URL))

    loggedin_message = home_page.nav.get_loggedin_msg()
    assert test_data.LOGGED_IN_MSG in loggedin_message, f"Expected message: '{test_data.LOGGED_IN_MSG}', actual message: '{loggedin_message}'"

    home_page.add_to_cart(0)
    home_page.add_to_cart(1)
    home_page.add_to_cart(2)
    home_page.nav.click_cart()
    
    current_url = driver.current_url
    assert test_data.CART_PAGE_PATH in current_url, f"Expected URL: '{test_data.CART_PAGE_PATH}', actual URL: {current_url}"

    cart_page = CartPage(driver)
    cart_page.click_checkout_button()

    wait.until(EC.url_contains(test_data.CHECKOUT_PAGE_PATH))

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

    WebDriverWait(driver, 5).until(EC.url_contains(test_data.PAYMENT_PAGE_PATH))

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

    WebDriverWait(driver, 5).until(EC.url_contains("payment_done"))

    # Delete account
    payment_page.nav.click_delete_account()

    account_deleted_title = driver.find_element(By.CSS_SELECTOR, "h2[data-qa='account-deleted']").text
    assert account_deleted_title == test_data.ACCOUNT_DELETED_TITLE, f"Expected title: '{test_data.ACCOUNT_DELETED_TITLE}', actual title: '{account_deleted_title}'"

    continue_button = driver.find_element(By.CSS_SELECTOR, "a[data-qa='continue-button']")
    continue_button.click()