from pages.base_page import BasePage
import test_data
from selenium.webdriver.common.by import By

class LoginPage(BasePage):

    URL = f"{test_data.BASE_URL}{test_data.LOGIN_PAGE_PATH}"

    def __init__(self, driver):
        super().__init__(driver)

    def enter_email(self, email):
        email_field = self.driver.find_element(By.CSS_SELECTOR, ".login-form input[data-qa='login-email']")
        email_field.send_keys(email)

    def enter_password(self, password):
        password_field = self.driver.find_element(By.CSS_SELECTOR, ".login-form input[data-qa='login-password']")
        password_field.send_keys(password)

    def click_login_button(self):
        login_button = self.driver.find_element(By.CSS_SELECTOR, ".login-form button[data-qa='login-button']")
        login_button.click()