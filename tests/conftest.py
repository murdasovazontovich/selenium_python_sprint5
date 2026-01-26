import pytest
from selenium import webdriver
from tests.curl import *


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(main_site)
    yield driver
    driver.quit()
