from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class CheckoutPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def get_address_details(self):
        full_name = self.driver.find_element(By.CSS_SELECTOR, "li.address_firstname").text.split(" ")
        title = full_name[0].split(".")[0].lower()
        first_name = full_name[1]
        last_name = full_name[2]
        company_name = self.driver.find_elements(By.CSS_SELECTOR, "#address_delivery li")[2].text
        address_1 = self.driver.find_elements(By.CSS_SELECTOR, "#address_delivery li")[3].text
        address_2 = self.driver.find_elements(By.CSS_SELECTOR, "#address_delivery li")[4].text
        full_location = self.driver.find_elements(By.CSS_SELECTOR, "#address_delivery li")[5].text.split(" ")
        city = full_location[0]
        state = full_location[1]
        post_code = full_location[2]
        country = self.driver.find_element(By.CSS_SELECTOR, "#address_delivery li.address_country_name").text
        phone_num = self.driver.find_element(By.CSS_SELECTOR, "#address_delivery li.address_phone").text

        return {
            "title": title,
            "first_name": first_name,
            "last_name": last_name,
            "company_name": company_name,
            "address_1": address_1,
            "address_2": address_2,
            "city": city,
            "state": state,
            "post_code": post_code,
            "country": country,
            "phone_num": phone_num
        }
    
    def get_order_details(self):
        products = self.driver.find_elements(By.XPATH, "//tr[contains(@id, 'product')]")
        order_details = []
        '''
        items = [[item_name, item_price, item_qty, item_total]]
        '''
        for product in products:
            item_name = product.find_element(By.XPATH, "/td[@class='cart_description']//a").text
            item_price = product.find_element(By.XPATH, "/td[@class='cart_price']/p").text.split(" ")[1]
            item_qty = product.find_element(By.XPATH, "/td[@class='cart_quantity']/button").text
            item_total = product.find_element(By.XPATH, "/td[@class='cart_total']/p").text.split(" ")[1]
            order_details.append([item_name, item_price, item_qty, item_total])

        return order_details
    
    def enter_message(self, message):
        self.driver.find_element(By.CSS_SELECTOR, "#ordermsg textarea").send_keys(message)
        
    def click_payment_btn(self):
        self.driver.find_element(By.CSS_SELECTOR, "a[href='/payment']").click()