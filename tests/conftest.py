import pytest
from selenium.webdriver.chrome.webdriver import WebDriver

@pytest.fixture
def driver():
    driver = WebDriver()
    yield driver
    driver.quit()