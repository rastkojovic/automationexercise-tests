from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.product_details_page import ProductDetailsPage
import test_data
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

def test_open_products_page(driver):

    home_page = HomePage(driver)
    home_page.open()

    current_url = driver.current_url
    homepage_title = home_page.get_title()

    WebDriverWait(driver, 5).until(expected_conditions.url_contains(test_data.BASE_URL))

    assert test_data.BASE_URL in current_url, f"Expected URL: '{test_data.BASE_URL}', actual URL: '{current_url}'"
    assert homepage_title == test_data.HOMEPAGE_TITLE, f"Expected H1 text: '{test_data.HOMEPAGE_TITLE}', actual H1 text: '{homepage_title}'"

    home_page.click_products()

    WebDriverWait(driver, 5).until(expected_conditions.url_contains(test_data.PRODUCTS_PAGE_PATH))

    current_url = driver.current_url
    assert  test_data.PRODUCTS_PAGE_PATH in current_url, f"Expected URL: '{test_data.PRODUCTS_PAGE_PATH}', actual URL: '{current_url}'"

    product_element_list = driver.find_elements(By.CLASS_NAME, "col-sm-4")

    assert product_element_list, f"Products not found!"

    product_page = ProductPage(driver)
    product_page.view_product(1)

    WebDriverWait(driver, 5).until(expected_conditions.url_contains(test_data.PRODUCT_DETAILS_PAGE_PATH))

    PRODUCT1_DETAILS_PATH = f"{test_data.PRODUCT_DETAILS_PAGE_PATH}/1"

    current_url = driver.current_url
    assert PRODUCT1_DETAILS_PATH in current_url, f"Expected URL: '{PRODUCT1_DETAILS_PATH}', actual URL: '{current_url}'"

    product_details_page = ProductDetailsPage(driver)
    product_details = product_details_page.get_product_details()

    assert product_details["name"] == test_data.PRODUCT1_NAME, f"Expected name: '{test_data.PRODUCT1_NAME}', actual name: '{product_details['name']}'"
    assert product_details["category"] == test_data.PRODUCT1_CATEGORY, f"Expected category: '{test_data.PRODUCT1_CATEGORY}', actual category: '{product_details['category']}'"
    assert product_details["price"] == test_data.PRODUCT1_PRICE, f"Expected price: '{test_data.PRODUCT1_PRICE}', actual price: '{product_details['price']}'"
    assert product_details["availability"] == test_data.PRODUCT1_AVAILABILITY, f"Expected availability: '{test_data.PRODUCT1_AVAILABILITY}', actual availability: '{product_details['availability']}'"
    assert product_details["condition"] == test_data.PRODUCT1_CONDITION, f"Expected condition: '{test_data.PRODUCT1_CONDITION}', actual condition: '{product_details['condition']}'"
    assert product_details["brand"] == test_data.PRODUCT1_BRAND, f"Expected brand: '{test_data.PRODUCT1_BRAND}', actual brand: '{product_details['brand']}'"