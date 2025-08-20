from components.navbar import NavBar

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.nav = NavBar(self.driver)

    def open(self):
        self.driver.get(self.URL)

