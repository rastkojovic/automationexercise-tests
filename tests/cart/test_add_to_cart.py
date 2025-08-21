from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
import test_data

def test_add_to_cart(driver):
    '''
    Test Case 12: Add Products in Cart
    '''

    home_page = HomePage(driver)
    home_page.open()

    home_page_h1_text = home_page.get_h1_text()

    assert test_data.BASE_URL in driver.current_url, f"Expected URL to contain {test_data.BASE_URL}, but got {driver.current_url}"
    assert test_data.HOMEPAGE_H1_TEXT == home_page_h1_text, f"Expected H1 text: {test_data.HOMEPAGE_H1_TEXT}, actual H1 text: {home_page_h1_text}"

    home_page.nav.click_products()

    product_page = ProductPage(driver)
    product_page.add_to_cart(0)
    product_page.dialogue_continue_shopping()

    product_page.add_to_cart(1)
    product_page.dialogue_view_cart()

    WebDriverWait(driver, 5).until(EC.url_contains(test_data.CART_PAGE_PATH))

    cart_page = CartPage(driver)
    cart_items = cart_page.get_cart_items()

    # Product 1
    assert cart_items[0].name == test_data.PRODUCT1_NAME, f"Expected product name: {test_data.PRODUCT1_NAME}, actual: {cart_items[0].name}"
    assert cart_items[0].price == test_data.PRODUCT1_PRICE, f"Expected product price: {test_data.PRODUCT1_PRICE}, actual: {cart_items[0].price}"
    assert cart_items[0].quantity == "1", f"Expected product quantity: 1, actual: {cart_items[0].quantity}"
    assert cart_items[0].total == test_data.PRODUCT1_PRICE, f"Expected product total: {test_data.PRODUCT1_PRICE}, actual: {cart_items[0].total}"

    # Product 2
    assert cart_items[1].name == test_data.PRODUCT2_NAME, f"Expected product name: {test_data.PRODUCT2_NAME}, actual: {cart_items[1].name}"
    assert cart_items[1].price == test_data.PRODUCT2_PRICE, f"Expected product price: {test_data.PRODUCT2_PRICE}, actual: {cart_items[1].price}"
    assert cart_items[1].quantity == "1", f"Expected product quantity: 1, actual: {cart_items[1].quantity}"
    assert cart_items[1].total == test_data.PRODUCT2_PRICE, f"Expected product total: {test_data.PRODUCT2_PRICE}, actual: {cart_items[1].total}"
