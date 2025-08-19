from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class CartItem:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.total = self.price * self.quantity

class CartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def enter_subscription_email(self, email):
        email_field = self.driver.find_element(By.ID, "susbscribe_email")
        email_field.send_keys(email)

    def click_subscribe(self):
        self.driver.find_element(By.ID, "subscribe").click()

    def get_subscription_success_message(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#footer .alert-success").text
    
    def get_cart_items(self):
        cart_items = []
        item_elements = self.driver.find_elements(By.CSS_SELECTOR, "tbody tr")
        for item in item_elements:
            item_name = item.find_element(By.CSS_SELECTOR, ".cart_description a").text
            item_price = float(item.find_element(By.CSS_SELECTOR, ".cart_price p").text.split(" ")[1])
            item_quantity = int(item.find_element(By.CSS_SELECTOR, ".cart_quantity button").text)
            cart_item = CartItem(item_name, item_price, item_quantity)
            cart_items.append(cart_item)
        return cart_items
    
    def item_in_cart(self, item_name):
        cart_items = self.get_cart_items()
        for item in cart_items:
            if item.item_name == item_name:
                return False
        return True
    
    def click_checkout_button(self):
        self.driver.find_element(By.CSS_SELECTOR, "a.check_out").click()

    def click_register_login_link(self):
        self.driver.find_element(By.CSS_SELECTOR, ".modal-body a[href='/login']").click()

    def remove_from_cart(self, item_index):
        item = self.driver.find_elements(By.CSS_SELECTOR, "tbody tr")[item_index]
        item.find_element(By.CSS_SELECTOR, ".cart_quantity_delete").click()