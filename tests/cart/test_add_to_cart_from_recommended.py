import test_data
from pages.home_page import HomePage
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By

def test_add_to_cart_from_recommended(driver):
    '''
    Test Case 22: Add to cart from Recommended items
    '''

    home_page = HomePage(driver)
    home_page.open()

    recommended_items = driver.find_element(By.CLASS_NAME, "recommended_items")
    # Using scroll origin and pause to make the scroll visible
    ActionChains(driver).scroll_from_origin(ScrollOrigin.from_element(recommended_items), 0, 200).pause(1).scroll_to_element(recommended_items).perform()

    recommended_items_title = home_page.get_recommended_items_title()
    expected_title = "RECOMMENDED ITEMS"
    assert recommended_items_title == expected_title, f"Expected title: '{expected_title}', actual title: '{recommended_items_title}'"

    # TODO: Click on 'Add To Cart' on Recommended product
    # TODO: Click on 'View Cart' button
    # TODO: Verify that product is displayed in cart page