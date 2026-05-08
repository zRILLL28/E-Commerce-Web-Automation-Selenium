from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    """
    Page Object untuk halaman Keranjang Belanja.
    """

    # Locators
    PAGE_TITLE        = (By.CLASS_NAME, "title")
    CART_ITEMS        = (By.CLASS_NAME, "cart_item")
    ITEM_NAMES        = (By.CLASS_NAME, "inventory_item_name")
    ITEM_PRICES       = (By.CLASS_NAME, "inventory_item_price")
    REMOVE_BUTTON     = (By.CSS_SELECTOR, "button[id^='remove']")
    CONTINUE_SHOPPING = (By.ID, "continue-shopping")
    CHECKOUT_BUTTON   = (By.ID, "checkout")

    def get_page_title(self):
        return self.get_text(*self.PAGE_TITLE)

    def get_cart_item_count(self):
        return len(self.driver.find_elements(*self.CART_ITEMS))

    def get_cart_item_names(self):
        elements = self.driver.find_elements(*self.ITEM_NAMES)
        return [el.text for el in elements]

    def remove_first_item(self):
        buttons = self.driver.find_elements(*self.REMOVE_BUTTON)
        if buttons:
            buttons[0].click()

    def continue_shopping(self):
        self.click(*self.CONTINUE_SHOPPING)

    def proceed_to_checkout(self):
        self.click(*self.CHECKOUT_BUTTON)

    def is_cart_empty(self):
        return self.get_cart_item_count() == 0
