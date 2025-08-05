from pages.base_page import BasePage
from test_data import HOMEPAGE_URL
from selenium.webdriver.common.by import By

class HomePage(BasePage):

    URL = HOMEPAGE_URL

    def __init__(self, driver):
        super().__init__(driver)

    def get_h1_text(self):
        h1_element = self.driver.find_element(By.TAG_NAME, "h1")
        return h1_element.text
    
    def click_signup_login(self):
        signup_login_link = self.driver.find_element(By.CSS_SELECTOR, ".navbar-nav a[href='/login']")
        signup_login_link.click()

    def get_signup_form_title(self):
        signup_form_title = self.driver.find_element(By.CSS_SELECTOR, "#form .signup-form h2").text
        return signup_form_title
    
    def get_login_form_title(self):
        login_form_title = self.driver.find_element(By.CSS_SELECTOR, "#form .login-form h2").text
        return login_form_title
    
    def delete_account(self):
        delete_account_element = self.driver.find_elements(By.CSS_SELECTOR, "ul.navbar-nav li")[4]
        delete_account_element.click()