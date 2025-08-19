from pages.home_page import HomePage
from pages.signup_page import SignupPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.payment_page import PaymentPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import test_data


def test_register_before_checkout(driver):
    
    home_page = HomePage(driver)
    home_page.open()

    wait = WebDriverWait(driver, 5)

    wait.until(expected_conditions.url_contains(test_data.BASE_URL))

    current_url = driver.current_url
    homepage_title = driver.find_element(By.TAG_NAME, "h1").text

    assert test_data.BASE_URL in current_url, f"Expected URL: '{test_data.BASE_URL}', actual URL: '{current_url}'"
    assert test_data.HOMEPAGE_TITLE in homepage_title, f"Expected title: '{test_data.HOMEPAGE_TITLE}', actual title: '{homepage_title}'"

    home_page.click_signup_login()

    wait.until(expected_conditions.url_contains(test_data.LOGIN_PAGE_PATH))
    # CREATE ACCOUNT
    signup_page = SignupPage(driver)
    signup_page.enter_name(test_data.NAME)
    signup_page.enter_email(test_data.EMAIL)
    signup_page.click_signup_button()

    wait.until(expected_conditions.url_contains(test_data.SIGNUP_PAGE_PATH))

    signup_page.select_title(test_data.TITLE)
    signup_page.enter_password(test_data.PASSWORD)
    signup_page.select_dob(day=test_data.DOB["day"], month=test_data.DOB["month"], year=test_data.DOB["year"])
    signup_page.check_newsletter()
    signup_page.check_special()
    signup_page.enter_first_name(test_data.NAME)
    signup_page.enter_last_name(test_data.LAST_NAME)
    signup_page.enter_company_name(test_data.COMPANY)
    signup_page.enter_address1(test_data.ADDRESS1)
    signup_page.enter_address2(test_data.ADDRESS2)
    signup_page.select_country(test_data.COUNTRY)
    signup_page.enter_state(test_data.STATE)
    signup_page.enter_city(test_data.CITY)
    signup_page.enter_zipcode(test_data.ZIP)
    signup_page.enter_mobile(test_data.PHONE_NUM)
    signup_page.create_account()

    account_created_title = driver.find_element(By.CSS_SELECTOR, "h2[data-qa='account-created']").text

    assert account_created_title == test_data.ACCOUNT_CREATED_TITLE, f"Expected H2 title: '{test_data.ACCOUNT_CREATED_TITLE}', actual H2 title: '{account_created_title}'"
    
    continue_button = driver.find_element(By.CSS_SELECTOR, "a[data-qa='continue-button']")
    continue_button.click()

    navbar_items = driver.find_elements(By.CSS_SELECTOR, ".navbar-nav li")
    logged_in_text = navbar_items[9].text.strip()

    assert logged_in_text == f"Logged in as {test_data.NAME}", f"Expected text: 'Logged in as {test_data.NAME}', actual text: '{logged_in_text}'"

    # ADD ITEMS TO CART
    home_page.add_to_cart(0)
    home_page.add_to_cart(1)
    home_page.add_to_cart(2)

    home_page.click_cart()

    wait.until(expected_conditions.url_contains(test_data.CART_PAGE_PATH))

    current_url = driver.current_url
    assert test_data.CART_PAGE_PATH in current_url, f"Expected URL: '{test_data.CART_PAGE_PATH}', actual URL: '{current_url}'"

    cart_page = CartPage(driver)
    cart_page.click_checkout_button()

    wait.until(expected_conditions.url_contains(test_data.CHECKOUT_PAGE_PATH))

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

    WebDriverWait(driver, 5).until(expected_conditions.url_contains(test_data.PAYMENT_PAGE_PATH))

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

    WebDriverWait(driver, 5).until(expected_conditions.url_contains("payment_done"))

    # Delete account
    delete_account_link = driver.find_element(By.CSS_SELECTOR, "a[href='/delete_account']")
    delete_account_link.click()

    WebDriverWait(driver, 5).until(expected_conditions.url_contains(test_data.DELETE_ACCOUNT_PAGE_PATH))

    account_deleted_title = driver.find_element(By.CSS_SELECTOR, "h2[data-qa='account-deleted']").text

    assert account_deleted_title == test_data.ACCOUNT_DELETED_TITLE, f"Expected title: '{test_data.ACCOUNT_DELETED_TITLE}', actual title: '{account_deleted_title}'"

    continue_button = driver.find_element(By.CSS_SELECTOR, "a[data-qa='continue-button']")
    continue_button.click()