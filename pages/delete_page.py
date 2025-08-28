from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import test_data

class DeletePage(BasePage):

    URL = f"{test_data.BASE_URL}{test_data.DELETE_ACCOUNT_PAGE_PATH}"

    def __init__(self, driver):
        super().__init__(driver)

    def get_account_deleted_title(self):
        return self.driver.find_element(By.CSS_SELECTOR, "h2[data-qa='account-deleted']").text
    
    def click_continue_btn(self):
        return self.driver.find_element(By.CSS_SELECTOR, "a[data-qa='continue-button']").click()