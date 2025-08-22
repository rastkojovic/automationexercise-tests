from pages.cart_page import CartPage
import test_data

def test_remove_from_cart(driver, home_page):
    '''
    Test Case 17: Remove Products From Cart
    '''

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