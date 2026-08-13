from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage


def test_valid_login():
    options = Options()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://www.saucedemo.com/")

        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        assert "inventory.html" in driver.current_url

    finally:
        driver.quit()