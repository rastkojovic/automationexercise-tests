from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import test_data
import os

class ContactPage(BasePage):

    URL = test_data.CONTACT_PAGE_PATH

    def __init__(self, driver):
        super().__init__(driver)

    def get_form_title(self):
        form_title = self.driver.find_element(By.CSS_SELECTOR, ".contact-form h2").text
        return form_title
    
    def enter_data(self, selector, data):
        input_field = self.driver.find_element(By.CSS_SELECTOR, selector)
        input_field.send_keys(data)
    
    def enter_name(self, name):
        self.enter_data("#contact-us-form input[name='name']", name)

    def enter_email(self, email):
        self.enter_data("#contact-us-form input[name='email']", email)

    def enter_subject(self, subject):
        self.enter_data("#contact-us-form input[name='subject']", subject)

    def enter_message(self, message):
        self.enter_data("#contact-us-form textarea[name='message']", message)

    def upload_file(self, file_path):
        file_path = os.path.abspath(file_path)
        file_upload = self.driver.find_element(By.CSS_SELECTOR, "input[type='file']")
        file_upload.send_keys(file_path)
    
    def submit(self):
        submit_button = self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
        submit_button.click()

    def get_success_msg(self):
        success_msg = self.driver.find_element(By.CSS_SELECTOR, ".alert-success").text
        return success_msg
    
    def click_home_button(self):
        home_button = self.driver.find_element(By.CSS_SELECTOR, "a.btn-success")
        home_button.click()