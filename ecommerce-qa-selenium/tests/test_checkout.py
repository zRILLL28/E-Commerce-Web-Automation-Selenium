import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils.test_data import (
    VALID_USER, VALID_CUSTOMER, INVALID_CUSTOMER,
    CHECKOUT_URL_SUFFIX, CONFIRMATION_URL_SUFFIX, ORDER_CONFIRMED_TEXT
)


class TestCheckout:
    """
    Test Suite: Fitur Checkout
    Target: https://www.saucedemo.com/checkout-step-one.html

    Test Cases:
    - TC_CHK_001: Checkout berhasil dengan data lengkap (end-to-end)
    - TC_CHK_002: Checkout gagal jika form kosong
    - TC_CHK_003: Summary menampilkan total harga yang benar
    - TC_CHK_004: Cancel pada step 2 mengembalikan ke halaman cart
    """

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.login_page = LoginPage(driver)
        self.inventory_page = InventoryPage(driver)
        self.cart_page = CartPage(driver)
        self.checkout_page = CheckoutPage(driver)

        # Setup: login → tambah produk → ke cart → ke checkout
        self.login_page.login(VALID_USER["username"], VALID_USER["password"])
        self.inventory_page.add_first_product_to_cart()
        self.inventory_page.go_to_cart()
        self.cart_page.proceed_to_checkout()

    def test_TC_CHK_001_successful_checkout(self):
        """TC_CHK_001: Checkout berhasil (end-to-end) hingga halaman konfirmasi."""
        # Step 1: Isi form
        self.checkout_page.fill_checkout_info(
            VALID_CUSTOMER["first_name"],
            VALID_CUSTOMER["last_name"],
            VALID_CUSTOMER["postal_code"]
        )
        self.checkout_page.click_continue()

        # Step 2: Klik Finish
        self.checkout_page.click_finish()

        # Verifikasi: Order Confirmed
        assert self.checkout_page.is_order_confirmed(), \
            "Halaman konfirmasi seharusnya tampil setelah checkout berhasil"

        confirmation_text = self.checkout_page.get_confirmation_header()
        assert ORDER_CONFIRMED_TEXT in confirmation_text, \
            f"Teks konfirmasi tidak sesuai. Dapat: '{confirmation_text}'"

        current_url = self.checkout_page.get_current_url()
        assert CONFIRMATION_URL_SUFFIX in current_url, \
            f"URL seharusnya mengandung '{CONFIRMATION_URL_SUFFIX}'. Dapat: {current_url}"

    def test_TC_CHK_002_checkout_with_empty_form(self):
        """TC_CHK_002: Checkout gagal jika form kosong."""
        self.checkout_page.fill_checkout_info(
            INVALID_CUSTOMER["first_name"],
            INVALID_CUSTOMER["last_name"],
            INVALID_CUSTOMER["postal_code"]
        )
        self.checkout_page.click_continue()

        assert self.checkout_page.is_error_displayed(), \
            "Error message seharusnya muncul jika form checkout kosong"
        error_text = self.checkout_page.get_error_message()
        assert "first name is required" in error_text.lower(), \
            f"Error message tidak sesuai: {error_text}"

    def test_TC_CHK_003_order_summary_shows_total(self):
        """TC_CHK_003: Halaman summary menampilkan subtotal, tax, dan total."""
        self.checkout_page.fill_checkout_info(
            VALID_CUSTOMER["first_name"],
            VALID_CUSTOMER["last_name"],
            VALID_CUSTOMER["postal_code"]
        )
        self.checkout_page.click_continue()

        subtotal = self.checkout_page.get_subtotal()
        tax = self.checkout_page.get_tax()
        total = self.checkout_page.get_total()

        assert "Item total" in subtotal, f"Subtotal tidak tampil: {subtotal}"
        assert "Tax" in tax, f"Tax tidak tampil: {tax}"
        assert "Total" in total, f"Total tidak tampil: {total}"

    def test_TC_CHK_004_cancel_on_step2_returns_to_cart(self):
        """TC_CHK_004: Menekan Cancel pada step 2 mengembalikan ke inventory."""
        self.checkout_page.fill_checkout_info(
            VALID_CUSTOMER["first_name"],
            VALID_CUSTOMER["last_name"],
            VALID_CUSTOMER["postal_code"]
        )
        self.checkout_page.click_continue()
        self.checkout_page.click_cancel()

        current_url = self.checkout_page.get_current_url()
        assert "inventory" in current_url, \
            f"Setelah cancel, seharusnya kembali ke inventory. URL: {current_url}"
