import pytest
import time
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils.test_data import VALID_USER, CART_URL_SUFFIX


class TestCart:
    """
    Test Suite: Fitur Keranjang Belanja
    Target: https://www.saucedemo.com/cart.html

    Test Cases:
    - TC_CART_001: Produk yang ditambahkan muncul di halaman cart
    - TC_CART_002: Menghapus produk dari cart berhasil
    - TC_CART_003: Cart kosong jika tidak ada produk ditambahkan
    - TC_CART_004: Tombol Continue Shopping mengembalikan ke halaman produk
    """

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.login_page = LoginPage(driver)
        self.inventory_page = InventoryPage(driver)
        self.cart_page = CartPage(driver)
        self.login_page.login(VALID_USER["username"], VALID_USER["password"])

    def test_TC_CART_001_product_appears_in_cart(self):
        """TC_CART_001: Produk yang ditambahkan muncul di halaman cart."""
        # Ambil nama produk pertama dari halaman inventory
        product_names = self.inventory_page.get_all_product_names()
        first_product = product_names[0]
        time.sleep(2)

        # Tambahkan produk pertama ke cart
        self.inventory_page.add_first_product_to_cart()
        self.inventory_page.go_to_cart()
        time.sleep(2)

        # Verifikasi URL
        current_url = self.cart_page.get_current_url()
        assert CART_URL_SUFFIX in current_url, \
            f"Seharusnya di halaman cart. URL: {current_url}"

        # Verifikasi produk ada di cart
        cart_items = self.cart_page.get_cart_item_names()
        assert first_product in cart_items, \
            f"Produk '{first_product}' seharusnya ada di cart. Items: {cart_items}"

    def test_TC_CART_002_remove_item_from_cart(self):
        """TC_CART_002: Menghapus produk dari cart berhasil."""
        #self.inventory_page.add_first_product_to_cart()
        self.inventory_page.go_to_cart()
        time.sleep(2)

        # Verifikasi ada item di cart
        count_before = self.cart_page.get_cart_item_count()
        assert count_before > 0, "Cart harus berisi minimal 1 item sebelum dihapus"
        time.sleep(2)

        # Hapus item
        self.cart_page.remove_first_item()
        count_after = self.cart_page.get_cart_item_count()
        time.sleep(2)

        assert count_after == count_before - 1, \
            f"Jumlah item seharusnya berkurang 1, dari {count_before} ke {count_before - 1}. Dapat: {count_after}"

    def test_TC_CART_003_empty_cart(self):
        """TC_CART_003: Cart kosong jika tidak ada produk ditambahkan."""
        self.inventory_page.go_to_cart()
        time.sleep(3)
        assert self.cart_page.is_cart_empty(), \
            "Cart seharusnya kosong jika tidak ada produk yang ditambahkan"

    def test_TC_CART_004_continue_shopping_button(self):
        """TC_CART_004: Tombol Continue Shopping mengembalikan ke halaman inventory."""
        self.inventory_page.go_to_cart()
        self.cart_page.continue_shopping()
        current_url = self.cart_page.get_current_url()
        assert "inventory" in current_url, \
            f"Seharusnya kembali ke halaman inventory. URL: {current_url}"
