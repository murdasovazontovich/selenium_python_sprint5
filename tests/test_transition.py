import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from tests.locators import Locators
from tests.curl import *



class TestTransition:
    def test_click_personal_account(self, driver):
        driver.find_element(*Locators.LOGIN_PERSONAL_ACC).click()
    
        assert driver.current_url == url_login


    def test_transition_to_conctructor_from_lk(self, driver):
        driver.find_element(*Locators.LOGIN_PERSONAL_ACC).click()
        driver.find_element(*Locators.BUTTON_CONSTRUCTOR).click()
        
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.BURGER_TEXT))
        

    def test_click_on_logo_from_lk(self, driver):
        driver.find_element(*Locators.LOGIN_PERSONAL_ACC).click()
        driver.find_element(*Locators.BUTTON_LOGO).click()
        
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.BURGER_TEXT))

