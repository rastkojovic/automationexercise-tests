from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class ProductDetailsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def get_product_details(self):

        product_information_element = self.driver.find_element(By.CLASS_NAME, "product-information")
        name = product_information_element.find_element(By.TAG_NAME, "h2").text
        category = product_information_element.find_elements(By.TAG_NAME, "p")[0].text.split(":")[1].strip()
        price = product_information_element.find_element(By.CSS_SELECTOR, "span > span").text
        availability = product_information_element.find_elements(By.TAG_NAME, "p")[1].text.split(":")[1].strip()
        condition = product_information_element.find_elements(By.TAG_NAME, "p")[2].text.split(":")[1].strip()
        brand = product_information_element.find_elements(By.TAG_NAME, "p")[3].text.split(":")[1].strip()

        return {
            "name": name,
            "category": category,
            "price": price,
            "availability": availability,
            "condition": condition,
            "brand": brand
        }

    def add_to_cart(self):
        self.driver.find_element(By.CSS_SELECTOR, ".product-information button.cart").click()

    def set_quantity(self, quantity):
        quantity_input = self.driver.find_element(By.ID, "quantity")
        quantity_input.clear()
        quantity_input.send_keys(str(quantity))

    def view_cart(self):
        self.driver.find_element(By.CSS_SELECTOR, ".modal-content a[href='/view_cart']").click()