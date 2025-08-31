from pages.base_page import BasePage
from components.dialogue import Dialogue
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
import test_data
import re

class HomePage(BasePage):

    URL = test_data.BASE_URL

    def __init__(self, driver):
        super().__init__(driver)
        self.dialogue = Dialogue(self.driver)

    def open(self):
        super().open()
        WebDriverWait(self.driver, 10).until(EC.url_matches(rf"{re.escape(test_data.BASE_URL)}(/)?$"))

    def assert_is_open(self):
        homepage_title = self.get_heading()
        assert test_data.BASE_URL in self.driver.current_url, f"Expected URL: '{test_data.BASE_URL}', actual URL: '{self.driver.current_url}'"
        assert test_data.HOMEPAGE_TITLE in homepage_title, f"Expected title: '{test_data.HOMEPAGE_TITLE}', actual title: '{homepage_title}'"

    def get_heading(self):
        h1_element = self.driver.find_element(By.TAG_NAME, "h1")
        return h1_element.text

    def get_signup_form_title(self):
        signup_form_title = self.driver.find_element(By.CSS_SELECTOR, "#form .signup-form h2").text
        return signup_form_title
    
    def get_login_form_title(self):
        login_form_title = self.driver.find_element(By.CSS_SELECTOR, "#form .login-form h2").text
        return login_form_title

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
        element_container = self.driver.find_element(By.XPATH, f"(//div[@class='single-products'])[{item_index}]")
        ActionChains(self.driver).move_to_element(element_container).perform()
        link_locator = f"(//div[@class='overlay-content'])[{item_index}]//a[contains(@class, 'add-to-cart')]"
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.all_of(
            EC.visibility_of_element_located((By.XPATH, link_locator))
        ))
        wait.until(EC.element_to_be_clickable((By.XPATH, link_locator))).click()

    def get_item_details(self, product_index):
        product_info = self.driver.find_elements(By.CSS_SELECTOR, ".productinfo")[product_index]
        return {
            "name": product_info.find_element(By.CSS_SELECTOR, "p").text,
            "price": product_info.find_element(By.CSS_SELECTOR, "h2").text
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
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.visibility_of_element_located((By.XPATH, f"//*[@id='{category_name}']//a[normalize-space(text())='{subcategory_name}']")))
            element = wait.until(EC.element_to_be_clickable((By.XPATH, f"//*[@id='{category_name}']//a[normalize-space(text())='{subcategory_name}']")))
            element.click()

    def get_recommended_items_title(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".recommended_items h2").text
    
    def recommended_add_to_cart(self, product_name):
        locator = f"//div[contains(@class, 'recommended_items')]//p[text()='{product_name}']/following-sibling::a"
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.visibility_of_element_located((By.XPATH, locator)))
        wait.until(EC.element_to_be_clickable((By.XPATH, locator))).click()

    def click_up(self):
        self.driver.find_element(By.ID, "scrollUp").click()
        
        