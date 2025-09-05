from selenium.webdriver.common.by import By
from core.utils import wait_for, element_text

class InternetLogin:
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    SUBMIT = (By.CSS_SELECTOR, "button[type='submit']")
    FLASH = (By.ID, "flash")

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def load(self):
        self.driver.get(self.url)

    def sign_in(self, user, pwd):
        wait_for(self.driver, self.USERNAME).send_keys(user)
        self.driver.find_element(*self.PASSWORD).send_keys(pwd)
        self.driver.find_element(*self.SUBMIT).click()

    def is_logged(self):
        return "/secure" in self.driver.current_url

    def error(self):
        return element_text(self.driver, self.FLASH).replace("×", "").strip()
