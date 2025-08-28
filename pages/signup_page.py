from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select
from pages.base_page import BasePage
import test_data

class SignupPage(BasePage):

    URL = f"{test_data.BASE_URL}{test_data.LOGIN_PAGE_PATH}"

    def __init__(self, driver):
        super().__init__(driver)

    def enter_name(self, name):
        name_field = self.driver.find_element(By.CSS_SELECTOR, "form[action='/signup'] input[data-qa='signup-name']")
        name_field.send_keys(name)
    
    def enter_email(self, email):
        email_field = self.driver.find_element(By.CSS_SELECTOR, "form[action='/signup'] input[data-qa='signup-email']")
        email_field.send_keys(email)

    def click_signup_button(self):
        signup_button = self.driver.find_element(By.CSS_SELECTOR, "form[action='/signup'] button[data-qa='signup-button']")
        signup_button.click()

    def get_signup_form_title(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".signup-form h2").text
    
    def get_signup_page_title(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".login-form h2.title").text
    
    def get_account_created_title(self):
        return self.driver.find_element(By.CSS_SELECTOR, "h2[data-qa='account-created']").text
    
    def click_continue_btn(self):
        return self.driver.find_element(By.CSS_SELECTOR, "a[data-qa='continue-button']").click()
    
    def get_error_msg(self):
        try:
            error_msg = self.driver.find_element(By.CSS_SELECTOR, ".signup-form p").text
            return error_msg
        except NoSuchElementException:
            return "Error message not found!"

    def select_title(self, title):

        match title:
            case 'mr':
                title_radio = self.driver.find_element(By.ID, "id_gender1")
                title_radio.click()
            case 'mrs':
                title_radio = self.driver.find_element(By.ID, "id_gender2")
                title_radio.click()

    def enter_password(self, password):
        password_field = self.driver.find_element(By.ID, "password")
        password_field.send_keys(password)

    
    def select_dob(self, day, month, year):
        day_select = self.driver.find_element(By.CSS_SELECTOR, "select#days")
        Select(day_select).select_by_visible_text(day)

        month_select = self.driver.find_element(By.CSS_SELECTOR, "select#months")
        Select(month_select).select_by_visible_text(month)

        year_select = self.driver.find_element(By.CSS_SELECTOR, "select#years")
        Select(year_select).select_by_visible_text(year)


    def check_checkbox(self, id):
        self.driver.find_element(By.ID, id).click()

    def check_newsletter(self):
        self.check_checkbox("newsletter")

    def check_special(self):
        self.check_checkbox("optin")

    def enter_field(self, id, info):
        self.driver.find_element(By.ID, id).send_keys(info)

    def enter_first_name(self, first_name):
        self.enter_field(id="first_name", info=first_name)

    def enter_last_name(self, last_name):
        self.enter_field(id="last_name", info=last_name)

    def enter_company_name(self, company_name):
        self.enter_field(id="company", info=company_name)

    def enter_address1(self, address1):
        self.enter_field(id="address1", info=address1)

    def enter_address2(self, address2):
        self.enter_field(id="address2", info=address2)

    def select_country(self, country):
        Select(self.driver.find_element(By.ID, "country")).select_by_visible_text(country)

    def enter_state(self, state):
        self.enter_field(id="state", info=state)

    def enter_city(self, city):
        self.enter_field(id="city", info=city)

    def enter_zipcode(self, zipcode):
        self.enter_field(id="zipcode", info=zipcode)

    def enter_mobile(self, mobile_number):
        self.enter_field(id="mobile_number", info=mobile_number)

    def create_account(self):
        self.driver.find_element(By.CSS_SELECTOR, "button[data-qa='create-account']").click()