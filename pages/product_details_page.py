from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class ProductDetailsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def normalize_text(self, text):
        return " ".join(text.replace("\xa0", " ").split())

    def get_product_details(self):

        product_information_element = self.driver.find_element(By.CLASS_NAME, "product-information")
        name = self.normalize_text(product_information_element.find_element(By.TAG_NAME, "h2").text)
        category = self.normalize_text(product_information_element.find_elements(By.TAG_NAME, "p")[0].text.split(":")[1])
        price = self.normalize_text(product_information_element.find_element(By.CSS_SELECTOR, "span > span").text)
        availability = self.normalize_text(product_information_element.find_elements(By.TAG_NAME, "p")[1].text.split(":")[1])
        condition = self.normalize_text(product_information_element.find_elements(By.TAG_NAME, "p")[2].text.split(":")[1])
        brand = self.normalize_text(product_information_element.find_elements(By.TAG_NAME, "p")[3].text.split(":")[1])

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

    def get_review_title(self):
        return self.driver.find_element(By.CSS_SELECTOR, "a[href='#reviews']").text
    
    def _enter_data(self, id, data):
        self.driver.find_element(By.ID, id).send_keys(data)

    def enter_email(self, email):
        self._enter_data("email", email)

    def enter_name(self, name):
        self._enter_data("name", name)

    def enter_review(self, review):
        self._enter_data("review", review)

    def submit_review(self):
        self.driver.find_element(By.ID, "button-review").click()

    def get_review_message(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#review-section span")))
        return self.driver.find_element(By.CSS_SELECTOR, "#review-section span").text