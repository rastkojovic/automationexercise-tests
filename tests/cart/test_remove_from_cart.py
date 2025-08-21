from pages.home_page import HomePage
from pages.cart_page import CartPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import test_data

def test_remove_from_cart(driver):
    '''
    Test Case 17: Remove Products From Cart
    '''

    home_page = HomePage(driver)
    home_page.open()

    homepage_title = home_page.get_title()

    wait = WebDriverWait(driver, 5)
    wait.until(EC.url_contains(test_data.BASE_URL))

    assert test_data.BASE_URL in driver.current_url, f"Expected URL: '{test_data.BASE_URL}', actual URL: '{driver.current_url}'"
    assert test_data.HOMEPAGE_TITLE in homepage_title, f"Expected title: '{test_data.HOMEPAGE_TITLE}', actual title: '{homepage_title}'"

    home_page.add_to_cart(0)
    home_page.add_to_cart(1)
    home_page.add_to_cart(2)
    home_page.nav.click_cart()

    assert test_data.CART_PAGE_PATH in driver.current_url, f"Expected URL: '{test_data.CART_PAGE_PATH}', actual URL: '{driver.current_url}'"

    cart_page = CartPage(driver)

    item_index = 1
    # GET ITEM ARRAY BEFORE REMOVAL
    cart_items = cart_page.get_cart_items()
    item_at_index = cart_items[item_index]
    cart_page.remove_from_cart(item_index)

    # CHECK ITEMS AFTER REMOVAL
    cart_items = cart_page.get_cart_items()
    assert item_at_index not in cart_items, f"Expected to remove item '{item_index.name}' but it is still present!"