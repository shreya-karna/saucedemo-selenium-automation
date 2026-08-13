from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.login_page import LoginPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage


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
        inventory_page = InventoryPage(driver)
        inventory_page.add_backpack_to_cart()

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