from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import test_data

class ProductPage(BasePage):

    URL = f"{test_data.BASE_URL}{test_data.PRODUCTS_PAGE_PATH}"

    def __init__(self, driver):
        super().__init__(driver)

    def view_product(self, product_index):
        product_element_list = self.driver.find_elements(By.CLASS_NAME, "col-sm-4")
        selected_product = product_element_list[product_index]
        view_product_link = selected_product.find_element(By.LINK_TEXT, "View Product")
        view_product_link.click()

    def search(self, product_name):
        search_field = self.driver.find_element(By.ID, "search_product")
        search_field.send_keys(product_name)
        search_button = self.driver.find_element(By.ID, "submit_search")
        search_button.click()

    def get_search_title(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".features_items h2.title").text
    
    def get_product_names(self):
        product_elements = self.driver.find_elements(By.CSS_SELECTOR, ".features_items .productinfo p")
        return [name.text for name in product_elements]
    
    def check_search_results(self, product_name, product_names):
        for name in product_names:
            print(name)
            if product_name not in name.lower():
                return False
        return True
    
    def add_to_cart(self, product_index):
        add_to_cart_btn_xpath = f"(//div[@class='single-products'])[{product_index + 1}]//div[contains(@class,'productinfo')]/a[contains(@class,'add-to-cart')]"
        add_to_cart_button = self.driver.find_element(By.XPATH, add_to_cart_btn_xpath)
        add_to_cart_button.click()

    def dialogue_continue_shopping(self):
        modal_content = self.driver.find_element(By.CSS_SELECTOR, ".modal-content")
        continue_shopping_button = modal_content.find_element(By.CSS_SELECTOR, ".modal-footer button")
        continue_shopping_button.click()

    def dialogue_view_cart(self):
        modal_content = self.driver.find_element(By.CSS_SELECTOR, ".modal-content")
        view_cart_link = modal_content.find_element(By.LINK_TEXT, "View Cart")
        view_cart_link.click()