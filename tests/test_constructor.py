import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from tests.locators import Locators
from tests.helpers import generate_email
from tests.helpers import Data
import time 

class TestConstructor:
    def test_transition_to_souce(self, driver):
        driver.find_element(*Locators.BUTTON_SAUCE).click()
        first_sauce = driver.find_element(*Locators.FIRST_SPICY_SAUCE)

        assert first_sauce.get_attribute('alt') == "Соус Spicy-X"

    def test_transition_to_topping(self, driver):
        driver.find_element(*Locators.BUTTON_TOPPING).click()
        first_topping = driver.find_element(*Locators.FIRST_TOPPING)

        assert first_topping.get_attribute('alt') == 'Мясо бессмертных моллюсков Protostomia'

    
    def test_transition_to_bread(self, driver):
        driver.find_element(*Locators.BUTTON_TOPPING).click()
        time.sleep(2)
        driver.find_element(*Locators.BUTTON_BREAD).click()
        time.sleep(2)
        first_bread = driver.find_element(*Locators.FIRST_BREAD)

        assert first_bread.get_attribute('alt') == 'Флюоресцентная булка R2-D3'
    