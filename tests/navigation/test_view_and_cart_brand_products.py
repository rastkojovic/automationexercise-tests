from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import test_data
from pages.home_page import HomePage
from pages.product_page import ProductPage

def test_view_and_cart_brand_products(driver):
    '''
    Test Case 19: View & Cart Brand Products
    '''
    
    home_page = HomePage(driver)
    home_page.open()

    wait = WebDriverWait(driver, 5)

    assert test_data.BASE_URL in driver.current_url, f"Expected URL: '{test_data.BASE_URL}', actual URL: '{driver.current_url}'"

    home_page.nav.click_products()

    assert test_data.PRODUCTS_PAGE_PATH in driver.current_url, f"Expected URL: '{test_data.PRODUCTS_PAGE_PATH}', actual URL: '{driver.current_url}'"

    product_page = ProductPage(driver)
    brand_names = product_page.get_brand_names()
    
    assert test_data.BRAND_NAMES == brand_names, f"Expected brand names '{test_data.BRAND_NAMES}', actual brand names: '{brand_names}'"
    # Select brand Kookie Kids
    product_page.select_brand("Kookie Kids")
    wait.until(EC.url_contains("Kookie%20Kids"))

    assert "Kookie%20Kids" in driver.current_url, f"Expected URL to contain 'Kookie%20Kids', actual URL: '{driver.current_url}'"

    kookiekids_products = ['Full Sleeves Top Cherry - Pink', 'Little Girls Mr. Panda Shirt', 'Cotton Mull Embroidered Dress']
    visible_products = product_page.get_product_names()
    assert visible_products == kookiekids_products, f"Expected products: '{kookiekids_products}', actual products: '{visible_products}' "

    # Select brand MADAME
    product_page.select_brand("Madame")
    wait.until(EC.url_contains("Madame"))

    assert "Madame" in driver.current_url, f"Expected URL to contain 'Madame', actual URL: {driver.current_url}"
    madame_products = ['Sleeveless Dress', 'Stylish Dress', 'Madame Top For Women', 'Rose Pink Embroidered Maxi Dress', 'Beautiful Peacock Blue Cotton Linen Saree']
    visible_products = product_page.get_product_names()
    assert visible_products == madame_products, f"Expected products: '{madame_products}', actual products: '{visible_products}' "