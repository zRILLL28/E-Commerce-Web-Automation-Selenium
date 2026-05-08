import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.test_data import VALID_USER, EXPECTED_PRODUCT_COUNT


class TestProduct:
    """
    Test Suite: Fitur Produk / Inventory
    Target: https://www.saucedemo.com/inventory.html

    Test Cases:
    - TC_PROD_001: Halaman produk tampil setelah login
    - TC_PROD_002: Jumlah produk sesuai yang diharapkan (6 produk)
    - TC_PROD_003: Sort produk A-Z
    - TC_PROD_004: Sort produk harga rendah ke tinggi
    - TC_PROD_005: Tambah produk ke keranjang menaikkan cart badge
    """

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.login_page = LoginPage(driver)
        self.inventory_page = InventoryPage(driver)
        # Login dulu sebelum setiap test produk
        self.login_page.login(VALID_USER["username"], VALID_USER["password"])

    def test_TC_PROD_001_inventory_page_loads(self):
        """TC_PROD_001: Halaman inventory tampil dengan judul yang benar."""
        title = self.inventory_page.get_page_title()
        assert title == "Products", \
            f"Judul halaman seharusnya 'Products', tapi dapat: '{title}'"

    def test_TC_PROD_002_product_count(self):
        """TC_PROD_002: Jumlah produk yang tampil sesuai (6 produk)."""
        count = self.inventory_page.get_product_count()
        assert count == EXPECTED_PRODUCT_COUNT, \
            f"Jumlah produk seharusnya {EXPECTED_PRODUCT_COUNT}, tapi dapat: {count}"

    def test_TC_PROD_003_sort_a_to_z(self):
        """TC_PROD_003: Sort produk A-Z menghasilkan urutan alphabetical."""
        self.inventory_page.sort_products("az")
        names = self.inventory_page.get_all_product_names()
        assert names == sorted(names), \
            f"Produk tidak urut A-Z. Urutan saat ini: {names}"

    def test_TC_PROD_004_sort_price_low_to_high(self):
        """TC_PROD_004: Sort harga rendah ke tinggi menghasilkan urutan ascending."""
        self.inventory_page.sort_products("lohi")
        prices = self.inventory_page.get_all_product_prices()
        assert prices == sorted(prices), \
            f"Harga tidak urut dari rendah ke tinggi. Urutan: {prices}"

    def test_TC_PROD_005_add_to_cart_updates_badge(self):
        """TC_PROD_005: Menambah produk ke cart menaikkan angka cart badge."""
        initial_count = self.inventory_page.get_cart_count()
        self.inventory_page.add_first_product_to_cart()
        new_count = self.inventory_page.get_cart_count()
        assert new_count == initial_count + 1, \
            f"Cart badge seharusnya naik 1, dari {initial_count} menjadi {initial_count + 1}. Tapi dapat: {new_count}"
