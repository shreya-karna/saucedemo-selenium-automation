from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.login_page import LoginPage
from pages.checkout_page import CheckoutPage


def test_complete_checkout():
    options = Options()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://www.saucedemo.com/")

        # Login
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        # Add first product to cart
        driver.find_element(
            "id", "add-to-cart-sauce-labs-backpack"
        ).click()

        # Checkout
        checkout_page = CheckoutPage(driver)
        checkout_page.open_cart()
        checkout_page.click_checkout()

        checkout_page.enter_customer_information(
            "Test",
            "User",
            "12345"
        )

        checkout_page.click_continue()
        checkout_page.click_finish()

        assert checkout_page.is_order_complete()

    finally:
        driver.quit()