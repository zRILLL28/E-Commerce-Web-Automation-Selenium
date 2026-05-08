# 🛒 E-Commerce QA Automation — Selenium Python

Proyek **Software Quality Assurance (SQA)** berbasis **Selenium + Python + Pytest** untuk menguji fungsionalitas web e-commerce demo [SauceDemo](https://www.saucedemo.com).

---

## 📋 Fitur yang Diuji

| Modul | Test Case | Jumlah TC |
|---|---|---|
| 🔐 **Login** | Login valid, locked user, kredensial salah, field kosong, logout | 5 |
| 🛍️ **Produk** | Tampilan halaman, jumlah produk, sorting A-Z, sorting harga, add to cart | 5 |
| 🛒 **Keranjang** | Produk muncul di cart, hapus item, cart kosong, continue shopping | 4 |
| 💳 **Checkout** | Checkout sukses (E2E), form kosong, summary harga, cancel | 4 |

**Total: 18 Test Cases**

---

## 🗂️ Struktur Project

```
ecommerce-qa-selenium/
│
├── pages/                  # Page Object Model (POM)
│   ├── base_page.py        # Base class dengan method umum
│   ├── login_page.py       # Halaman Login
│   ├── inventory_page.py   # Halaman Daftar Produk
│   ├── cart_page.py        # Halaman Keranjang
│   └── checkout_page.py    # Halaman Checkout & Konfirmasi
│
├── tests/                  # Test Cases
│   ├── test_login.py       # Test Suite: Login
│   ├── test_product.py     # Test Suite: Produk
│   ├── test_cart.py        # Test Suite: Keranjang
│   └── test_checkout.py    # Test Suite: Checkout
│
├── utils/
│   └── test_data.py        # Data untuk test (user, customer info, dll)
│
├── reports/                # HTML report hasil test (auto-generated)
├── screenshots/            # Screenshot otomatis jika test gagal
│
├── conftest.py             # Konfigurasi WebDriver & Fixtures
├── pytest.ini              # Konfigurasi Pytest
├── requirements.txt        # Dependency Python
└── README.md
```

---

## ⚙️ Cara Menjalankan

### 1. Clone Repository
```bash
git clone https://github.com/<username>/ecommerce-qa-selenium.git
cd ecommerce-qa-selenium
```

### 2. Buat Virtual Environment
```bash
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Jalankan Semua Test
```bash
pytest
```

### 5. Jalankan Headless (tanpa buka browser)
```bash
pytest --headless
```

### 6. Jalankan Test Spesifik
```bash
# Hanya test login
pytest tests/test_login.py

# Hanya test checkout
pytest tests/test_checkout.py

# Jalankan satu test case tertentu
pytest tests/test_login.py::TestLogin::test_TC_LOGIN_001_login_valid
```

### 7. Lihat Laporan HTML
Setelah test selesai, buka file berikut di browser:
```
reports/report.html
```

---

## 🛠️ Tech Stack

| Tool | Versi | Fungsi |
|---|---|---|
| Python | 3.10+ | Bahasa pemrograman utama |
| Selenium | 4.x | Browser automation |
| Pytest | 8.x | Test framework |
| pytest-html | 4.x | HTML report generator |
| WebDriver Manager | 4.x | Auto-download ChromeDriver |

---

## 🏗️ Konsep yang Diterapkan

- **Page Object Model (POM)** — Memisahkan logika UI dari logika test
- **Fixtures** — Setup/teardown WebDriver yang reusable
- **Screenshot on Failure** — Otomatis capture screenshot jika test gagal
- **Test Data Separation** — Data test dipisah ke file `utils/test_data.py`
- **HTML Reporting** — Laporan test yang mudah dibaca

---

## 📸 Contoh Laporan

Laporan HTML akan otomatis dibuat di folder `reports/` setelah menjalankan test. Laporan ini berisi:
- ✅ Status tiap test case (PASSED / FAILED / ERROR)
- ⏱️ Durasi eksekusi
- 🔍 Detail error jika test gagal
- 📸 Link screenshot untuk test yang gagal

---

> Proyek ini menggunakan situs demo publik [SauceDemo](https://www.saucedemo.com) yang memang disediakan khusus untuk latihan automation testing.
