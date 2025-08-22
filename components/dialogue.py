from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Dialogue:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def continue_shopping(self):
        continue_shopping_button = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".modal-content .modal-footer button")))
        continue_shopping_button.click()

    def view_cart(self):
        view_cart_link = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".modal-content .modal-body a[href='/view_cart']")))
        view_cart_link.click()