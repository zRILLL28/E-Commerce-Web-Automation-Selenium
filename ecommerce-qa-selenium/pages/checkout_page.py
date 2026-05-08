from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    """
    Page Object untuk halaman Checkout (Step 1 & 2) dan Order Confirmation.
    """

    # Step 1 - Info Pembeli
    FIRST_NAME_INPUT  = (By.ID, "first-name")
    LAST_NAME_INPUT   = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON   = (By.ID, "continue")
    ERROR_MESSAGE     = (By.CSS_SELECTOR, "[data-test='error']")

    # Step 2 - Review Order
    SUMMARY_SUBTOTAL  = (By.CLASS_NAME, "summary_subtotal_label")
    SUMMARY_TAX       = (By.CLASS_NAME, "summary_tax_label")
    SUMMARY_TOTAL     = (By.CLASS_NAME, "summary_total_label")
    FINISH_BUTTON     = (By.ID, "finish")
    CANCEL_BUTTON     = (By.ID, "cancel")

    # Confirmation
    COMPLETE_HEADER   = (By.CLASS_NAME, "complete-header")
    COMPLETE_TEXT     = (By.CLASS_NAME, "complete-text")
    BACK_HOME_BUTTON  = (By.ID, "back-to-products")

    # ── Step 1 Methods ──────────────────────────────────
    def enter_first_name(self, first_name):
        self.type(*self.FIRST_NAME_INPUT, first_name)

    def enter_last_name(self, last_name):
        self.type(*self.LAST_NAME_INPUT, last_name)

    def enter_postal_code(self, postal_code):
        self.type(*self.POSTAL_CODE_INPUT, postal_code)

    def fill_checkout_info(self, first_name, last_name, postal_code):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_postal_code(postal_code)

    def click_continue(self):
        self.click(*self.CONTINUE_BUTTON)

    def get_error_message(self):
        return self.get_text(*self.ERROR_MESSAGE)

    def is_error_displayed(self):
        return self.is_visible(*self.ERROR_MESSAGE)

    # ── Step 2 Methods ──────────────────────────────────
    def get_subtotal(self):
        return self.get_text(*self.SUMMARY_SUBTOTAL)

    def get_tax(self):
        return self.get_text(*self.SUMMARY_TAX)

    def get_total(self):
        return self.get_text(*self.SUMMARY_TOTAL)

    def click_finish(self):
        self.click(*self.FINISH_BUTTON)

    def click_cancel(self):
        self.click(*self.CANCEL_BUTTON)

    # ── Confirmation Methods ─────────────────────────────
    def get_confirmation_header(self):
        return self.get_text(*self.COMPLETE_HEADER)

    def is_order_confirmed(self):
        return self.is_visible(*self.COMPLETE_HEADER)

    def back_to_home(self):
        self.click(*self.BACK_HOME_BUTTON)
