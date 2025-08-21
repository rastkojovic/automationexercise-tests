from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
import test_data
import re


class NavBar:


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def _click_link(self, locator, path):
        element = self.wait.until(EC.element_to_be_clickable(locator))

        try:
            element.click()
        except Exception:
            ActionChains(self.driver).move_to_element(element).pause(0.5).click().perform()
        self.wait.until(EC.url_contains(path))

    def click_home(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".navbar-nav a[href='/']"))).click()
        self.wait.until(
            EC.all_of(EC.url_matches(rf"{re.escape(test_data.BASE_URL)}(/)?$"), # Avoid trailing / issue
                      lambda d: test_data.HOMEPAGE_TITLE.lower() in d.find_element(By.TAG_NAME, "h1").text.lower(),
                      ))


    def click_products(self):
        self._click_link((By.CSS_SELECTOR, f".navbar-nav a[href='{test_data.PRODUCTS_PAGE_PATH}']"), test_data.PRODUCTS_PAGE_PATH)
        self.wait.until(lambda d: "all products" in d.find_element(By.CSS_SELECTOR, "h2.title").text.lower())

    def click_cart(self):
        self._click_link((By.CSS_SELECTOR, f".navbar-nav a[href='{test_data.CART_PAGE_PATH}']"), test_data.CART_PAGE_PATH)
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a.check_out")))

    def click_signup_login(self):
        self._click_link((By.CSS_SELECTOR, f".navbar-nav a[href='{test_data.LOGIN_PAGE_PATH}']"), test_data.LOGIN_PAGE_PATH)
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "login-form")))

    def click_contact(self):
        self._click_link((By.CSS_SELECTOR, f".navbar-nav a[href='{test_data.CONTACT_PAGE_PATH}']"), test_data.CONTACT_PAGE_PATH)
        self.wait.until(lambda d: "contact us" in d.find_element(By.XPATH, "(//h2[contains(@class,'title')])[1]").text.lower())

    def click_delete_account(self):
        self._click_link((By.CSS_SELECTOR, f".navbar-nav a[href='{test_data.DELETE_ACCOUNT_PAGE_PATH}']"), test_data.DELETE_ACCOUNT_PAGE_PATH)
        self.wait.until(lambda d: "account deleted!" in d.find_element(By.CSS_SELECTOR, "h2.title").text.lower())

    def click_testcases(self):
        self._click_link((By.CSS_SELECTOR, f".navbar-nav a[href='{test_data.TEST_CASES_PAGE_PATH}']"), test_data.TEST_CASES_PAGE_PATH)
        self.wait.until(lambda d: "test cases" in d.find_element(By.CSS_SELECTOR, "h2.title").text.lower())

    def get_loggedin_msg(self):
        navbar_items = self.driver.find_elements(By.CSS_SELECTOR, "ul.navbar-nav li")

        for li in navbar_items:
            if test_data.LOGGED_IN_MSG in li.text:
                return li.text
        return ""