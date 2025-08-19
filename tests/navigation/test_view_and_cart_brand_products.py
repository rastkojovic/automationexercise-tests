from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import test_data
from pages.home_page import HomePage
from pages.product_page import ProductPage

def test_view_and_cart_brand_products(driver):
    
    home_page = HomePage(driver)
    home_page.open()

    wait = WebDriverWait(driver, 5)
    wait.until(expected_conditions.url_contains(test_data.BASE_URL))

    current_url = driver.current_url
    assert test_data.BASE_URL in current_url, f"Expected URL: '{test_data.BASE_URL}', actual URL: '{current_url}'"

    home_page.click_products()
    wait.until(expected_conditions.url_contains(test_data.PRODUCTS_PAGE_PATH))

    current_url = driver.current_url
    assert test_data.PRODUCTS_PAGE_PATH in current_url, f"Expected URL: '{test_data.PRODUCTS_PAGE_PATH}', actual URL: '{current_url}'"

    product_page = ProductPage(driver)
    brand_names = product_page.get_brand_names()
    
    assert test_data.BRAND_NAMES == brand_names, f"Expected brand names '{test_data.BRAND_NAMES}', actual brand names: '{brand_names}'"
    # Select brand Kookie Kids
    product_page.select_brand("Kookie Kids")
    wait.until(expected_conditions.url_contains("Kookie%20Kids"))

    current_url = driver.current_url
    assert "Kookie%20Kids" in current_url, f"Expected URL to contain 'Kookie%20Kids', actual URL: '{current_url}'"