from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class InventoryPage(BasePage):
    """
    Page Object untuk halaman Produk (Inventory).
    """

    # Locators
    PAGE_TITLE       = (By.CLASS_NAME, "title")
    PRODUCT_ITEMS    = (By.CLASS_NAME, "inventory_item")
    PRODUCT_NAMES    = (By.CLASS_NAME, "inventory_item_name")
    PRODUCT_PRICES   = (By.CLASS_NAME, "inventory_item_price")
    ADD_TO_CART_BTN  = (By.CSS_SELECTOR, "button[id^='add-to-cart']")
    CART_BADGE       = (By.CLASS_NAME, "shopping_cart_badge")
    CART_ICON        = (By.CLASS_NAME, "shopping_cart_link")
    SORT_DROPDOWN    = (By.CLASS_NAME, "product_sort_container")
    BURGER_MENU      = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK      = (By.ID, "logout_sidebar_link")

    def get_page_title(self):
        return self.get_text(*self.PAGE_TITLE)

    def get_all_product_names(self):
        elements = self.driver.find_elements(*self.PRODUCT_NAMES)
        return [el.text for el in elements]

    def get_all_product_prices(self):
        elements = self.driver.find_elements(*self.PRODUCT_PRICES)
        return [float(el.text.replace("$", "")) for el in elements]

    def get_product_count(self):
        return len(self.driver.find_elements(*self.PRODUCT_ITEMS))

    def add_first_product_to_cart(self):
        buttons = self.driver.find_elements(*self.ADD_TO_CART_BTN)
        if buttons:
            buttons[0].click()

    def add_product_by_index(self, index=0):
        buttons = self.driver.find_elements(*self.ADD_TO_CART_BTN)
        buttons[index].click()

    def get_cart_count(self):
        try:
            return int(self.get_text(*self.CART_BADGE))
        except Exception:
            return 0

    def go_to_cart(self):
        self.click(*self.CART_ICON)

    def sort_products(self, option_value):
        """
        option_value: 'az', 'za', 'lohi', 'hilo'
        """
        from selenium.webdriver.support.ui import Select
        dropdown = self.find(*self.SORT_DROPDOWN)
        Select(dropdown).select_by_value(option_value)

    def logout(self):
        self.click(*self.BURGER_MENU)
        self.click(*self.LOGOUT_LINK)
