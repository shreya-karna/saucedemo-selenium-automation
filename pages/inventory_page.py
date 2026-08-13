from selenium.webdriver.common.by import By

class InventoryPage:

    INVENTORY_CONTAINER = (By.ID, "inventory_container")
    PRODUCT_ITEMS = (By.CLASS_NAME, "inventory_item")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    ADD_BACKPACK_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")

    def __init__(self, driver):
        self.driver = driver

    def is_inventory_displayed(self):
        return self.driver.find_element(*self.INVENTORY_CONTAINER).is_displayed()

    def get_product_count(self):
        return len(self.driver.find_elements(*self.PRODUCT_ITEMS))

    def add_backpack_to_cart(self):
        self.driver.find_element(*self.ADD_BACKPACK_BUTTON).click()

    def click_cart(self):
        self.driver.find_element(*self.CART_LINK).click()