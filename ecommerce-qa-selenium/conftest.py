import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--headless", action="store_true", default=False, help="Run browser in headless mode")


@pytest.fixture(scope="session")
def driver(request):
    """
    Setup WebDriver session.
    Scope 'session' means browser dibuka sekali untuk semua test.
    """
    options = Options()

    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.default_content_setting_values.notifications": 2,
        "autofill.profile_enabled": False,
        "autofill.credit_card_enabled": False
    }

    # Jalankan headless jika pakai flag --headless
    if request.config.getoption("--headless"):
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-notifications")
    options.add_argument("--incognito")
    #options.add_argument("user-data-dir=./chrome-automation-profile")
    options.add_experimental_option("prefs", prefs)
    options.add_argument("--disable-save-password-bubble")
    options.add_argument("--disable-features=PasswordLeakDetection")

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    #driver = webdriver.Chrome(
        #service=Service(ChromeDriverManager().install()),
        #options=options

    driver.implicitly_wait(10)

    yield driver

    driver.quit()


@pytest.fixture(autouse=True)
def screenshot_on_failure(request, driver):
    """
    Otomatis ambil screenshot jika test gagal.
    """
    yield
    if request.node.rep_call.failed:
        test_name = request.node.name
        screenshot_path = f"screenshots/{test_name}.png"
        driver.save_screenshot(screenshot_path)
        print(f"\n📸 Screenshot saved: {screenshot_path}")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
