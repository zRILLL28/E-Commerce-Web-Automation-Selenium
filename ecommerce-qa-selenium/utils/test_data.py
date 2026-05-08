"""
Test data untuk semua test case.
Menggunakan akun dari situs demo: https://www.saucedemo.com
"""

# ── Valid Credentials ──────────────────────────────────────
VALID_USER = {
    "username": "standard_user",
    "password": "secret_sauce"
}

LOCKED_USER = {
    "username": "locked_out_user",
    "password": "secret_sauce"
}

PROBLEM_USER = {
    "username": "problem_user",
    "password": "secret_sauce"
}

# ── Invalid Credentials ───────────────────────────────────
INVALID_USER = {
    "username": "wrong_user",
    "password": "wrong_password"
}

EMPTY_CREDENTIALS = {
    "username": "",
    "password": ""
}

# ── Customer Info ─────────────────────────────────────────
VALID_CUSTOMER = {
    "first_name": "Budi",
    "last_name": "Santoso",
    "postal_code": "12345"
}

INVALID_CUSTOMER = {
    "first_name": "",
    "last_name": "",
    "postal_code": ""
}

# ── Expected Values ───────────────────────────────────────
EXPECTED_PRODUCT_COUNT = 6
INVENTORY_URL_SUFFIX = "/inventory.html"
CART_URL_SUFFIX = "/cart.html"
CHECKOUT_URL_SUFFIX = "/checkout-step-one.html"
CONFIRMATION_URL_SUFFIX = "/checkout-complete.html"
ORDER_CONFIRMED_TEXT = "Thank you for your order!"
