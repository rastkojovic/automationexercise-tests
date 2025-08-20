from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import test_data
import re

class HomePage(BasePage):

    URL = test_data.BASE_URL

    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        super().open()
        WebDriverWait.until(EC.url_matches(rf"{re.escape(test_data.BASE_URL)}(/)?$"))

    def get_title(self):
        h1_element = self.driver.find_element(By.TAG_NAME, "h1")
        return h1_element.text

    def get_signup_form_title(self):
        signup_form_title = self.driver.find_element(By.CSS_SELECTOR, "#form .signup-form h2").text
        return signup_form_title
    
    def get_login_form_title(self):
        login_form_title = self.driver.find_element(By.CSS_SELECTOR, "#form .login-form h2").text
        return login_form_title
    
    def logout(self):
        logout_link = self.driver.find_element(By.CSS_SELECTOR, ".navbar-nav a[href='/logout']")
        logout_link.click()

    def enter_subscription_email(self, email):
        email_field = self.driver.find_element(By.CSS_SELECTOR, ".searchform input[type='email']")
        email_field.send_keys(email)

    def click_subscribe(self):
        self.driver.find_element(By.ID, "subscribe").click()

    def get_subscription_success_message(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#footer .alert-success").text
    
    def view_product(self, product_index):
        product_link = self.driver.find_elements(By.CSS_SELECTOR, ".choose a")[product_index]
        product_link.click()

    def add_to_cart(self, item_index):
        item_list = self.driver.find_elements(By.CSS_SELECTOR, ".single-products")
        item_list[item_index].find_element(By.CSS_SELECTOR, "a.add-to-cart").click()
        continue_shopping_btn = self.driver.find_element(By.CSS_SELECTOR, ".modal-dialog .modal-footer button")
        continue_shopping_btn.click()

    def get_item_details(self, product_index):
        product_info = self.driver.find_elements(By.CSS_SELECTOR, ".productinfo")[product_index]
        return {
            "name": product_info.find_element(By.CSS_SELECTOR, "p").text,
            "price": float(product_info.find_element(By.CSS_SELECTOR, "h2").text.split(" ")[1])
        }
    
    def get_category_names(self):
        category_elements = self.driver.find_elements(By.CSS_SELECTOR, "#accordian .panel-title a")
        category_names = [name.text for name in category_elements]
        return category_names
    

    def select_category(self, category_name, subcategory_name=False):
        category_links = self.driver.find_elements(By.CSS_SELECTOR, "#accordian .panel-title a")
        category_index = 0
        match category_name:
            case "Women":
                pass
            case "Men":
                category_index = 1
            case "Kids":
                category_index = 2
            case _:
                print("Invalid category!")
        category_links[category_index].click()
        if subcategory_name is not False:
            wait = WebDriverWait(self.driver, 5)
            wait.until(EC.visibility_of_element_located((By.XPATH, f"//*[@id='{category_name}']//a[normalize-space(text())='{subcategory_name}']")))
            element = wait.until(EC.element_to_be_clickable((By.XPATH, f"//*[@id='{category_name}']//a[normalize-space(text())='{subcategory_name}']")))
            element.click()