import test_data
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.login_page import LoginPage


def test_search_products_verify_cart_after_login(driver):
    '''
    Test Case 20: Search Products and Verify Cart After Login
    '''
    
    home_page = HomePage(driver)
    home_page.open()

    assert test_data.BASE_URL in driver.current_url, f"Expected URL: '{test_data.BASE_URL}', actual URL: {driver.current_url}"

    home_page.nav.click_products()

    assert test_data.PRODUCTS_PAGE_PATH in driver.current_url, f"Expected URL: '{test_data.PRODUCTS_PAGE_PATH}', actual URL: {driver.current_url}"

    product_page = ProductPage(driver)
    search_term = "jeans"
    product_page.search_product(search_term)
    page_title = product_page.get_search_title()
    expected_title = "SEARCHED PRODUCTS"

    assert expected_title == page_title, f"Expected title: '{expected_title}', actual title: '{page_title}'"

    check = product_page.check_products(search_term)
    assert check is True, f"Some visible products don't match search term: {check[1]}"

    product_items = product_page.get_product_names()
    product_num = len(product_items)
    for i in range(product_num):
        product_page.add_to_cart(i)
        product_page.dialogue_continue_shopping()

    product_page.nav.click_cart()

    cart_page = CartPage(driver)
    # Check if all added items are in cart
    for product_name in product_items:
        assert cart_page.item_in_cart(product_name), f"Item '{product_name}' not in cart!"

    cart_page.nav.click_signup_login()

    login_page = LoginPage(driver)
    login_page.enter_email(test_data.EMAIL)
    login_page.enter_password(test_data.PASSWORD)
    login_page.click_login_button()

    login_page.nav.click_cart()
    # Check if all added items are in cart again
    for product_name in product_items:
        assert cart_page.item_in_cart(product_name), f"Item '{product_name}' not in cart!"