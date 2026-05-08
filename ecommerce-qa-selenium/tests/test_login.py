import pytest
import time
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.test_data import (
    VALID_USER, LOCKED_USER, INVALID_USER,
    EMPTY_CREDENTIALS, INVENTORY_URL_SUFFIX
)


class TestLogin:
    """
    Test Suite: Fitur Login
    Target: https://www.saucedemo.com

    Test Cases:
    - TC_LOGIN_001: Login berhasil dengan kredensial valid
    - TC_LOGIN_002: Login gagal dengan user yang dikunci (locked)
    - TC_LOGIN_003: Login gagal dengan kredensial salah
    - TC_LOGIN_004: Login gagal dengan field kosong
    - TC_LOGIN_005: Logout berhasil setelah login
    """

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.login_page = LoginPage(driver)
        self.inventory_page = InventoryPage(driver)

    def test_TC_LOGIN_001_login_valid(self):
        """TC_LOGIN_001: Login berhasil dengan user valid."""
        self.login_page.login(
            VALID_USER["username"],
            VALID_USER["password"]
        )
        current_url = self.login_page.get_current_url()
        assert INVENTORY_URL_SUFFIX in current_url, \
            f"Expected URL mengandung '{INVENTORY_URL_SUFFIX}', tapi dapat: {current_url}"

    def test_TC_LOGIN_002_locked_user(self):
        """TC_LOGIN_002: Login gagal untuk akun yang terkunci."""
        self.login_page.login(
            LOCKED_USER["username"],
            LOCKED_USER["password"]
        )
        assert self.login_page.is_error_displayed(), \
            "Error message seharusnya muncul untuk locked user"
        error_text = self.login_page.get_error_message()
        assert "locked out" in error_text.lower(), \
            f"Error message tidak sesuai: {error_text}"

    def test_TC_LOGIN_003_invalid_credentials(self):
        """TC_LOGIN_003: Login gagal dengan username/password salah."""
        self.login_page.login(
            INVALID_USER["username"],
            INVALID_USER["password"]
        )
        assert self.login_page.is_error_displayed(), \
            "Error message seharusnya muncul untuk kredensial salah"

    def test_TC_LOGIN_004_empty_credentials(self):
        """TC_LOGIN_004: Login gagal jika field kosong."""
        self.login_page.login(
            EMPTY_CREDENTIALS["username"],
            EMPTY_CREDENTIALS["password"]
        )
        assert self.login_page.is_error_displayed(), \
            "Error message seharusnya muncul jika field kosong"
        error_text = self.login_page.get_error_message()
        assert "username is required" in error_text.lower(), \
            f"Error message tidak sesuai: {error_text}"

    def test_TC_LOGIN_005_logout(self):
        """TC_LOGIN_005: Logout berhasil mengembalikan user ke halaman login."""
        self.login_page.login(
            VALID_USER["username"],
            VALID_USER["password"]
        )
        time.sleep (3)
        self.inventory_page.logout()
        current_url = self.login_page.get_current_url()
        assert current_url.endswith("/"), \
            f"Setelah logout, seharusnya kembali ke halaman login. URL: {current_url}"
