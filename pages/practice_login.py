from selenium.webdriver.common.by import By
from core.utils import wait_for, element_text

class PracticeLogin:
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    BTN = (By.ID, "submit")
    SUCCESS = (By.XPATH, "//h1[contains(.,'Logged In Successfully')]")
    ERROR = (By.ID, "error")

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def load(self):
        self.driver.get(self.url)

    def sign_in(self, user, pwd):
        wait_for(self.driver, self.USERNAME).send_keys(user)
        self.driver.find_element(*self.PASSWORD).send_keys(pwd)
        self.driver.find_element(*self.BTN).click()

    def is_logged(self):
        try:
            element_text(self.driver, self.SUCCESS)
            return True
        except:
            return False

    def error(self):
        return element_text(self.driver, self.ERROR) if self.driver.find_elements(*self.ERROR) else ""
