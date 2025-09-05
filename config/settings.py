# Base URLs of applications under test
URLS = {
    "saucedemo": "https://www.saucedemo.com",
    "internet": "https://the-internet.herokuapp.com/login",
    "practice": "https://practicetestautomation.com/practice-test-login/",
    "orangehrm": "https://opensource-demo.orangehrmlive.com/",
}

# Valid credentials for demo sites
CREDENTIALS = {
    "saucedemo": {"user": "standard_user", "pwd": "secret_sauce"},
    "internet": {"user": "tomsmith", "pwd": "SuperSecretPassword!"},
    "practice": {"user": "student", "pwd": "Password123"},
    "orangehrm": {"user": "Admin", "pwd": "admin123"},
}
