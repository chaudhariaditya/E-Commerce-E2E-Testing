
import pytest
from selenium import webdriver


@pytest.fixture()
def setup():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://www.ajio.com/")
    return driver




