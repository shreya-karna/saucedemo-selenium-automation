from selenium.webdriver.common.by import By


class CheckoutPage:

    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")

    def __init__(self, driver):
        self.driver = driver

    def open_cart(self):
        self.driver.find_element(*self.CART_LINK).click()

    def click_checkout(self):
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()

    def enter_customer_information(self, first_name, last_name, postal_code):
        self.driver.find_element(*self.FIRST_NAME).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME).send_keys(last_name)
        self.driver.find_element(*self.POSTAL_CODE).send_keys(postal_code)

    def click_continue(self):
        self.driver.find_element(*self.CONTINUE_BUTTON).click()

    def click_finish(self):
        self.driver.find_element(*self.FINISH_BUTTON).click()

    def is_order_complete(self):
        return self.driver.find_element(*self.COMPLETE_HEADER).is_displayed()