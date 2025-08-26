import test_data
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class AccountFlow:

    def __init__(self, driver):
        self.driver = driver

    def login(self, login_page):
        login_page.enter_email(test_data.EMAIL)
        login_page.enter_password(test_data.PASSWORD)
        login_page.click_login_button()

    def logout(self, home_page):
        home_page.nav.click_logout()

    def create(self, login_page, signup_page):

        wait = WebDriverWait(self.driver, 10)
        login_page.open()
        wait.until(EC.url_contains(test_data.LOGIN_PAGE_PATH))

        signup_page.enter_name(test_data.NAME)
        signup_page.enter_email(test_data.EMAIL)
        signup_page.click_signup_button()
        
        wait.until(EC.url_contains(test_data.SIGNUP_PAGE_PATH))

        signup_page.select_title(test_data.TITLE)
        signup_page.enter_password(test_data.PASSWORD)
        signup_page.select_dob(day=test_data.DOB["day"], month=test_data.DOB["month"], year=test_data.DOB["year"])
        signup_page.check_newsletter()
        signup_page.check_special()
        signup_page.enter_first_name(test_data.NAME)
        signup_page.enter_last_name(test_data.LAST_NAME)
        signup_page.enter_company_name(test_data.COMPANY)
        signup_page.enter_address1(test_data.ADDRESS1)
        signup_page.enter_address2(test_data.ADDRESS2)
        signup_page.select_country(test_data.COUNTRY)
        signup_page.enter_state(test_data.STATE)
        signup_page.enter_city(test_data.CITY)
        signup_page.enter_zipcode(test_data.ZIP)
        signup_page.enter_mobile(test_data.PHONE_NUM)
        signup_page.create_account()

        account_created_title = self.driver.find_element(By.CSS_SELECTOR, "h2[data-qa='account-created']").text
        assert account_created_title == test_data.ACCOUNT_CREATED_TITLE, f"Expected H2 title: '{test_data.ACCOUNT_CREATED_TITLE}', actual H2 title: '{account_created_title}'"
        
        continue_button = self.driver.find_element(By.CSS_SELECTOR, "a[data-qa='continue-button']")
        continue_button.click()

        logged_in_text = signup_page.nav.get_loggedin_msg()
        assert logged_in_text == f"Logged in as {test_data.NAME}", f"Expected text: 'Logged in as {test_data.NAME}', actual text: '{logged_in_text}'"

    def delete(self, page):
        page.nav.click_delete_account()
        account_deleted_title = self.driver.find_element(By.CSS_SELECTOR, "h2[data-qa='account-deleted']").text
        assert account_deleted_title == test_data.ACCOUNT_DELETED_TITLE, f"Expected title: '{test_data.ACCOUNT_DELETED_TITLE}', actual title: '{account_deleted_title}'"

        continue_button = self.driver.find_element(By.CSS_SELECTOR, "a[data-qa='continue-button']")
        continue_button.click()