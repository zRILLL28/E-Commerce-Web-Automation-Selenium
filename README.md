# 🛒 E-Commerce QA Automation — Selenium Python

**Software Quality Assurance (SQA)** project using **Selenium + Python + Pytest** to automate functional testing for the [SauceDemo](https://www.saucedemo.com) e-commerce demo website.

---

## 📋 Tested Features

| Module | Test Cases | Total TC |
|---|---|---|
| 🔐 **Login** | Valid login, locked user, invalid credentials, empty fields, logout | 5 |
| 🛍️ **Products** | Page display, product count, A-Z sorting, price sorting, add to cart | 5 |
| 🛒 **Cart** | Product displayed in cart, remove item, empty cart, continue shopping | 4 |
| 💳 **Checkout** | Successful checkout (E2E), empty form validation, price summary, cancel checkout | 4 |

**Total: 18 Test Cases**

---

## 🗂️ Project Structure

```bash
ecommerce-qa-selenium/
│
├── pages/                  # Page Object Model (POM)
│   ├── base_page.py        # Base class with reusable methods
│   ├── login_page.py       # Login Page
│   ├── inventory_page.py   # Product Inventory Page
│   ├── cart_page.py        # Cart Page
│   └── checkout_page.py    # Checkout & Confirmation Page
│
├── tests/                  # Test Cases
│   ├── test_login.py       # Login Test Suite
│   ├── test_product.py     # Product Test Suite
│   ├── test_cart.py        # Cart Test Suite
│   └── test_checkout.py    # Checkout Test Suite
│
├── utils/
│   └── test_data.py        # Test data (users, customer info, etc.)
│
├── reports/                # Auto-generated HTML test reports
├── screenshots/            # Automatically captured screenshots on failure
│
├── conftest.py             # WebDriver configuration & fixtures
├── pytest.ini              # Pytest configuration
├── requirements.txt        # Python dependencies
└── README.md
```

---

## ⚙️ How to Run

### 1. Clone Repository
```Bash
git clone https://github.com/zRILLL28/E-Commerce-Web-Automation-Selenium.git
cd E-Commerce-Web-Automation-Selenium
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run All Test
```bash
pytest
```

### 5. Run in Headless Mode (without opening browser)
```bash
pytest --headless
```

### 6. Run Specific Tests
```bash
# Run login tests only
pytest tests/test_login.py

# Only test checkout
pytest tests/test_checkout.py

# Run a specific test case
pytest tests/test_login.py::TestLogin::test_TC_LOGIN_001_login_valid
```

### 7. View HTML Report
After the test execution is completed, open the following file in your browser:
```
reports/report.html
```

---

## 🛠️ Tech Stack

| Tool | Versi | Fungsi |
|---|---|---|
| Python | 3.10+ | Main programming language |
| Selenium | 4.x | Browser automation |
| Pytest | 8.x | Test framework |
| pytest-html | 4.x | HTML report generator |
| WebDriver Manager | 4.x | Auto-download ChromeDriver |

---

## 🏗️ Implemented Concepts

- **Page Object Model (POM)** — Separates UI logic from test logic
- **Fixtures** — Reusable WebDriver setup/teardown
- **Screenshot on Failure** — Automatically captures screenshots when tests fail
- **Test Data Separation** — Test data stored separately in `utils/test_data.py`
- **HTML Reporting** — Easy-to-read test execution reports

---

## 📸 Report Example

An HTML report will be automatically generated inside the reports/ folder after running the tests. The report includes:
- ✅ Test case status (PASSED / FAILED / ERROR)
- ⏱️ Execution duration
- 🔍 Error details for failed tests
- 📸 Screenshot links for failed tests

---

## Demo
![Demo](Demo.gif)

---

> This project uses the public demo website [SauceDemo](https://www.saucedemo.com) which is specifically designed for automation testing practice.
