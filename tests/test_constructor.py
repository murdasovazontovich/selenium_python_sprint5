import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from tests.locators import Locators
from tests.helpers import generate_email
from tests.helpers import Data
from tests.curl import *


class TestConstructor:
    def test_transition_to_sauce(self, driver):
        driver.find_element(*Locators.BUTTON_SAUCE).click()
        active_tab = WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.SAUCE_TAB_ACTIVE))

        assert "tab_tab_type_current" in active_tab.get_attribute("class")

    def test_transition_to_topping(self, driver):
        driver.find_element(*Locators.BUTTON_TOPPING).click()
        active_tab = WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.TOPPING_TAB_ACTIVE))

        assert "tab_tab_type_current" in active_tab.get_attribute("class")
    
    def test_transition_to_bread(self, driver):
        driver.find_element(*Locators.BUTTON_TOPPING).click()
        driver.find_element(*Locators.BUTTON_BREAD).click()
        active_tab = WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.BREAD_TAB_ACTIVE))

        assert "tab_tab_type_current" in active_tab.get_attribute("class")