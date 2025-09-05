from selenium.webdriver.common.by import By
from core.utils import wait_for, element_text

class SauceDemoLogin:
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    BTN_LOGIN = (By.ID, "login-button")
    ERROR_MSG = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def load(self):
        self.driver.get(self.url)

    def sign_in(self, user, pwd):
        wait_for(self.driver, self.USERNAME).send_keys(user)
        self.driver.find_element(*self.PASSWORD).send_keys(pwd)
        self.driver.find_element(*self.BTN_LOGIN).click()

    def is_logged(self):
        return "inventory.html" in self.driver.current_url

    def error(self):
        try:
            return element_text(self.driver, self.ERROR_MSG)
        except:
            return ""
