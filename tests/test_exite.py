import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from tests.locators import Locators
from tests.helpers import Data


class TestExite:
    def test_exite_from_lk(self, driver):
        driver.find_element(*Locators.ENTRANCE_BUTTON).click()
        driver.find_element(*Locators.LOGIN_EMAIL).send_keys(Data.email)
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(Data.password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.LOGIN_PERSONAL_ACC).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.EXITE_BUTTON))
        driver.find_element(*Locators.EXITE_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON))
 
        assert '/login' in driver.current_url