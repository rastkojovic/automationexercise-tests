from pages.cart_page import CartPage
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By

def test_add_to_cart_from_recommended(driver, home_page):
    '''
    Test Case 22: Add to cart from Recommended items
    '''

    recommended_items = driver.find_element(By.CLASS_NAME, "recommended_items")
    # Using scroll origin and pause to make the scroll visible
    ActionChains(driver).scroll_from_origin(ScrollOrigin.from_element(recommended_items), 0, 200).pause(1).scroll_to_element(recommended_items).perform()

    recommended_items_title = home_page.get_recommended_items_title()
    expected_title = "RECOMMENDED ITEMS"
    assert recommended_items_title == expected_title, f"Expected title: '{expected_title}', actual title: '{recommended_items_title}'"

    product_name = "Men Tshirt"
    home_page.recommended_add_to_cart(product_name)
    home_page.dialogue.view_cart()

    cart_page = CartPage(driver)
    assert cart_page.item_in_cart(product_name), f"Product '{product_name}' not in cart!"