from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.product_page import ProductPage
from pages.cart_page import CartPage
import test_data

def test_add_to_cart(driver, home_page):
    '''
    Test Case 12: Add Products in Cart
    '''

    home_page.nav.click_products()

    product_page = ProductPage(driver)
    product_page.add_to_cart(0)
    product_page.dialogue.continue_shopping()

    product_page.add_to_cart(1)
    product_page.dialogue.view_cart()

    wait = WebDriverWait(driver, 10)
    wait.until(EC.url_contains(test_data.CART_PAGE_PATH))

    cart_page = CartPage(driver)
    cart_items = cart_page.get_cart_items()

    product1 = cart_items[0]
    assert product1.name == test_data.PRODUCT1_NAME, f"Expected product name: {test_data.PRODUCT1_NAME}, actual: {product1.name}"
    assert product1.price == test_data.PRODUCT1_PRICE, f"Expected product price: {test_data.PRODUCT1_PRICE}, actual: {product1.price}"
    assert product1.quantity == 1, f"Expected product quantity: 1, actual: {product1.quantity}"
    assert product1.total == test_data.PRODUCT1_PRICE, f"Expected product total: {test_data.PRODUCT1_PRICE}, actual: {product1.total}"

    product2 = cart_items[1]
    assert product2.name == test_data.PRODUCT2_NAME, f"Expected product name: {test_data.PRODUCT2_NAME}, actual: {product2.name}"
    assert product2.price == test_data.PRODUCT2_PRICE, f"Expected product price: {test_data.PRODUCT2_PRICE}, actual: {product2.price}"
    assert product2.quantity == 1, f"Expected product quantity: 1, actual: {product2.quantity}"
    assert product2.total == test_data.PRODUCT2_PRICE, f"Expected product total: {test_data.PRODUCT2_PRICE}, actual: {product2.total}"
