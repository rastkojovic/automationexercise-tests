from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from flows.account_flow import AccountFlow
import test_data
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def test_download_invoice(driver, home_page):
    '''
    Test Case 24: Download Invoice after purchase order
    '''

    home_page.add_to_cart(1)
    home_page.add_to_cart(3)
    home_page.add_to_cart(4)

    home_page.nav.click_cart()

    cart_page = CartPage(driver)
    cart_page.click_checkout_button()

    dialogue_locator = "//div[contains(@class, 'modal-dialog')]"
    link_locator = "//div[contains(@class, 'modal-dialog')]//a[@href='/login']"
    wait = WebDriverWait(driver, 10)
    wait.until(
        EC.all_of(
            EC.visibility_of_element_located((By.XPATH, dialogue_locator))),
            EC.element_to_be_clickable((By.XPATH, link_locator))
    )
    register_login_link = driver.find_element(By.XPATH, link_locator)
    register_login_link.click()

    # Create account [Example using AccountFlow]
    account_flow = AccountFlow(driver)
    account_flow.create()

    loggedin_msg = home_page.nav.get_loggedin_msg()
    assert test_data.LOGGED_IN_MSG in loggedin_msg, f"Expected message: '{test_data.LOGGED_IN_MSG}', actual message: '{loggedin_msg}'"

    home_page.nav.click_cart()

    cart_page.click_checkout_button()

    checkout_page = CheckoutPage(driver)
    address_details = checkout_page.get_address_details()

    assert test_data.TITLE == address_details["title"]
    assert test_data.NAME == address_details["first_name"]
    assert test_data.LAST_NAME == address_details["last_name"]
    assert test_data.COMPANY == address_details["company_name"]
    assert test_data.ADDRESS1 == address_details["address_1"]
    assert test_data.ADDRESS2 == address_details["address_2"]
    assert test_data.CITY == address_details["city"]
    assert test_data.STATE == address_details["state"]
    assert test_data.ZIP == address_details["post_code"]
    assert test_data.COUNTRY == address_details["country"]
    assert test_data.PHONE_NUM == address_details["phone_num"]

    account_flow.delete()