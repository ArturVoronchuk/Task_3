import pytest

import urls
from helpers import webdriver_factory
from helpers.user_generator import UserGenerator
from pages.account_page import AccountPage
from pages.header_page import HeaderPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.orders_feed_page import OrdersFeedPage
from pages.forgot_password_page import ForgotPasswordPage

@pytest.hookimpl(tryfirst=True)
def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="firefox",
        choices=["chrome", "firefox"],
        help="Browser name: chrome or firefox"
    )
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run browser in headless mode"
    )

@pytest.fixture(scope="function")
def driver(request):
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    driver = webdriver_factory.WebdriverFactory.get_webdriver(
        browser_name, headless=headless
    )
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def home_page(driver):
    page = HomePage(driver)
    page.go_to_url(urls.MAIN_PAGE_URL)
    return page

@pytest.fixture(scope="function")
def login_page(driver):
    page = LoginPage(driver)
    page.go_to_url(urls.LOGIN_PAGE_URL)   # → /login
    return page

@pytest.fixture(scope="function")
def forgot_password_page(driver):
    page = ForgotPasswordPage(driver)
    page.go_to_url(urls.FORGOT_PASSWORD_URL)
    return page

@pytest.fixture(scope="function")
def header_page(driver):
    page = HeaderPage(driver)
    return page

@pytest.fixture(scope="function")
def account_page(driver):
    page = AccountPage(driver)
    return page

@pytest.fixture(scope="function")
def orders_feed_page(driver):
    page = OrdersFeedPage(driver)
    page.go_to_url(urls.ORDERS_FEED_URL)
    return page

@pytest.fixture(scope="function")
def register_user():
    payload = UserGenerator.register_user()
    yield payload
    UserGenerator.delete_user(payload["email"], payload["password"])

@pytest.fixture(scope="function")
def registered_user_credentials(register_user):
    return register_user["email"], register_user["password"]
