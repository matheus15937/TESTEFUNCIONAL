from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_for(driver, locator, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))

def element_text(driver, locator, timeout=10):
    el = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))
    return el.text.strip()
