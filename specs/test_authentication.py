import pytest
from core.browser_factory import create_browser
from config.settings import URLS, CREDENTIALS
from pages.saucedemo_login import SauceDemoLogin
from pages.internet_login import InternetLogin
from pages.practice_login import PracticeLogin
from pages.orangehrm_login import OrangeHRMLogin

@pytest.fixture
def driver():
    drv = create_browser(headless=True)
    yield drv
    drv.quit()

@pytest.mark.smoke
@pytest.mark.parametrize("user,pwd,should_pass", [
    (CREDENTIALS["saucedemo"]["user"], CREDENTIALS["saucedemo"]["pwd"], True),
    ("wrong", "wrong", False),
])
def test_saucedemo(driver, user, pwd, should_pass):
    page = SauceDemoLogin(driver, URLS["saucedemo"])
    page.load()
    page.sign_in(user, pwd)
    assert page.is_logged() == should_pass

@pytest.mark.regression
@pytest.mark.parametrize("user,pwd,should_pass", [
    (CREDENTIALS["internet"]["user"], CREDENTIALS["internet"]["pwd"], True),
    ("bad", "SuperSecretPassword!", False),
])
def test_internet(driver, user, pwd, should_pass):
    page = InternetLogin(driver, URLS["internet"])
    page.load()
    page.sign_in(user, pwd)
    assert page.is_logged() == should_pass

@pytest.mark.regression
@pytest.mark.parametrize("user,pwd,should_pass", [
    (CREDENTIALS["practice"]["user"], CREDENTIALS["practice"]["pwd"], True),
    ("nope", "Password123", False),
])
def test_practice(driver, user, pwd, should_pass):
    page = PracticeLogin(driver, URLS["practice"])
    page.load()
    page.sign_in(user, pwd)
    assert page.is_logged() == should_pass

@pytest.mark.regression
@pytest.mark.parametrize("user,pwd,should_pass", [
    (CREDENTIALS["orangehrm"]["user"], CREDENTIALS["orangehrm"]["pwd"], True),
    ("Admin", "wrong", False),
])
def test_orangehrm(driver, user, pwd, should_pass):
    page = OrangeHRMLogin(driver, URLS["orangehrm"])
    page.load()
    page.sign_in(user, pwd)
    assert page.is_logged() == should_pass
