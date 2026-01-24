import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from tests.locators import Locators



class TestTransition:
    def test_click_personal_account(self, driver):
        driver.find_element(*Locators.LOGIN_PERSONAL_ACC).click()
        url_after = 'https://stellarburgers.education-services.ru/login'

        assert driver.current_url == url_after


    def test_transition_to_conctructor_from_lk(self, driver):
        driver.find_element(*Locators.LOGIN_PERSONAL_ACC).click()
        driver.find_element(*Locators.BUTTON_CONSTRUCTOR).click()
        burger_text = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.BURGER_TEXT))
        
        assert burger_text.is_displayed()

    def test_click_on_logo_from_lk(self, driver):
        driver.find_element(*Locators.LOGIN_PERSONAL_ACC).click()
        driver.find_element(*Locators.BUTTON_LOGO).click()
        burger_text = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.BURGER_TEXT))
        
        assert burger_text.is_displayed()

