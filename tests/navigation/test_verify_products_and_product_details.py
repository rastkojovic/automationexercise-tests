from pages.product_page import ProductPage
from pages.product_details_page import ProductDetailsPage
import test_data
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_verify_products_and_product_details(driver, home_page):
    '''
    Test Case 8: Verify All Products and product detail page
    '''

    home_page.nav.click_products()

    assert  test_data.PRODUCTS_PAGE_PATH in driver.current_url, f"Expected URL: '{test_data.PRODUCTS_PAGE_PATH}', actual URL: '{driver.current_url}'"

    product_element_list = driver.find_elements(By.CLASS_NAME, "col-sm-4")

    assert product_element_list, f"Products not found!"

    product_page = ProductPage(driver)
    # 0-based index, 1 -> 2nd product
    product_page.view_product(1)

    wait = WebDriverWait(driver, 10)
    wait.until(EC.url_contains(test_data.PRODUCT_DETAILS_PAGE_PATH))

    PRODUCT2_DETAILS_PATH = f"{test_data.PRODUCT_DETAILS_PAGE_PATH}/2"

    assert PRODUCT2_DETAILS_PATH in driver.current_url, f"Expected URL: '{PRODUCT2_DETAILS_PATH}', actual URL: '{driver.current_url}'"

    product_details_page = ProductDetailsPage(driver)
    product_details = product_details_page.get_product_details()

    assert product_details["name"] == test_data.PRODUCT2_NAME, f"Expected name: '{test_data.PRODUCT2_NAME}', actual name: '{product_details['name']}'"
    assert product_details["category"] == test_data.PRODUCT2_CATEGORY, f"Expected category: '{test_data.PRODUCT2_CATEGORY}', actual category: '{product_details['category']}'"
    assert product_details["price"] == test_data.PRODUCT2_PRICE, f"Expected price: '{test_data.PRODUCT2_PRICE}', actual price: '{product_details['price']}'"
    assert product_details["availability"] == test_data.PRODUCT2_AVAILABILITY, f"Expected availability: '{test_data.PRODUCT2_AVAILABILITY}', actual availability: '{product_details['availability']}'"
    assert product_details["condition"] == test_data.PRODUCT2_CONDITION, f"Expected condition: '{test_data.PRODUCT2_CONDITION}', actual condition: '{product_details['condition']}'"
    assert product_details["brand"] == test_data.PRODUCT2_BRAND, f"Expected brand: '{test_data.PRODUCT2_BRAND}', actual brand: '{product_details['brand']}'"