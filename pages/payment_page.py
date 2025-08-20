from pages.base_page import BasePage
import test_data
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException

class PaymentPage(BasePage):

    URL = test_data.PAYMENT_PAGE_PATH

    def __init__(self, driver):
        super().__init__(driver)

    def enter_data(self, name_attr, data):
        self.driver.find_element(By.CSS_SELECTOR, f"form[action='/payment'] input[name='{name_attr}']").send_keys(data)

    def enter_card_name(self, name):
        self.enter_data("name_on_card", name)

    def enter_card_num(self, card_num):
        self.enter_data("card_number", card_num)

    def enter_cvc(self, cvc):
        self.enter_data("cvc", cvc)

    def enter_expiry_month(self, expiry_month):
        self.enter_data("expiry_month", expiry_month)

    def enter_expiry_year(self, expiry_year):
        self.enter_data("expiry_year", expiry_year)

    def success_msg_present(self):
        try:
            wait = WebDriverWait(self.driver, 5, poll_frequency=0.1, ignored_exceptions=(StaleElementReferenceException,))
            wait.until(lambda driver: "hide" not in driver.find_element(By.ID, "success_message").get_attribute("class"))
            return test_data.ORDER_SUCCESS_MESSAGE == self.driver.find_element(By.CSS_SELECTOR, "#success_message .alert-success").text.strip()
        except TimeoutException:
            print("Error finding success_message element. Timout exception triggered!")
            return False

    def pay_and_confirm(self):
        self.driver.find_element(By.ID,"submit").click()