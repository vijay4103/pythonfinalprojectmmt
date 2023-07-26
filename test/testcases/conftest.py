import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome",
    )


@pytest.fixture(scope="class")
def setup(request):
    browser = request.config.getoption("browser_name")
    if browser == "chrome":
        path = Service("F:\\chromedriver_win32")
        driver = webdriver.Chrome(service=path)
        driver.get("https://www.makemytrip.com/")
        driver.implicitly_wait(30)
        driver.maximize_window()
        request.cls.driver = driver
        yield
        driver.close()
