from pages.cart_page import CartPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from pages.product_details_page import ProductDetailsPage
import test_data

def test_verify_qty_cart(driver, home_page):
    '''
    Test Case 13: Verify Product quantity in Cart
    '''

    product_index = 3
    product_quantity = 4
    item_details = home_page.get_item_details(product_index)
    home_page.view_product(product_index)

    wait = WebDriverWait(driver, 10)
    wait.until(EC.url_contains(test_data.PRODUCT_DETAILS_PAGE_PATH))

    assert f"{test_data.PRODUCT_DETAILS_PAGE_PATH}/{product_index + 1}" in driver.current_url, f"Expected URL '{test_data.PRODUCT_DETAILS_PAGE_PATH}/{product_index}', actual URL is '{driver.current_url}'"

    product_details_page = ProductDetailsPage(driver)
    product_details_page.set_quantity(product_quantity)
    product_details_page.add_to_cart()

    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".modal-content")))

    product_details_page.view_cart()

    wait.until(EC.url_contains(test_data.CART_PAGE_PATH))

    cart_page = CartPage(driver)
    cart_items = cart_page.get_cart_items()

    product = cart_items[0]
    assert product.name == item_details["name"], f"Expected item name '{item_details['name']}', but got '{product.name}'"
    assert product.price == item_details["price"], f"Expected item price '{item_details['price']}', but got '{product.price}'"
    assert product.quantity == product_quantity, f"Expected item quantity '{product_quantity}', but got '{product.quantity}'"