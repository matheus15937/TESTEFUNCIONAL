from selenium.webdriver.common.by import By
from core.utils import wait_for, element_text

class OrangeHRMLogin:
    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    BTN = (By.CSS_SELECTOR, "button[type='submit']")
    ALERT = (By.CSS_SELECTOR, ".oxd-alert-content--error")
    DASHBOARD = (By.CSS_SELECTOR, "h6.oxd-text")

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url.rstrip("/") + "/web/index.php/auth/login"

    def load(self):
        self.driver.get(self.url)

    def sign_in(self, user, pwd):
        wait_for(self.driver, self.USERNAME).send_keys(user)
        self.driver.find_element(*self.PASSWORD).send_keys(pwd)
        self.driver.find_element(*self.BTN).click()

    def is_logged(self):
        return "/dashboard" in self.driver.current_url

    def error(self):
        if self.driver.find_elements(*self.ALERT):
            return element_text(self.driver, self.ALERT)
        if self.driver.find_elements(By.XPATH, "//span[text()='Required']"):
            return "Required"
        return ""
