import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from tests.locators import Locators
from tests.helpers import Data
from tests.helpers import generate_email
from tests.helpers import generate_password
from tests.curl import *



class TestRegistration:
    def test_registration_name(self, driver):
        driver.find_element(*Locators.ENTRANCE_BUTTON).click()
        driver.find_element(*Locators.REG_BUTTON).click()
        name_input = driver.find_element(*Locators.REG_NAME)
        name_input.send_keys("Катерина")

        assert name_input.get_attribute("value") != ""

    def test_registration_email(self, driver):
        email = generate_email()  
        driver.find_element(*Locators.ENTRANCE_BUTTON).click()
        driver.find_element(*Locators.REG_BUTTON).click()
        email_input = driver.find_element(*Locators.REG_EMAIL)
        email_input.send_keys(email)

        assert '@' in email_input.get_attribute('value')
        assert '.' in email_input.get_attribute('value')

    def test_registration_password(self, driver):
        password = generate_password()  
        driver.find_element(*Locators.ENTRANCE_BUTTON).click()
        driver.find_element(*Locators.REG_BUTTON).click()
        password_input = driver.find_element(*Locators.REG_PASSWORD)
        password_input.send_keys(password)
        
        assert len(password_input.get_attribute('value')) >= 6
       
    def test_registration_short_password_shows_error(self, driver):
        driver.find_element(*Locators.ENTRANCE_BUTTON).click()
        driver.find_element(*Locators.REG_BUTTON).click()
        driver.find_element(*Locators.REG_NAME).send_keys("Катерина")
        driver.find_element(*Locators.REG_EMAIL).send_keys(Data.email)
        driver.find_element(*Locators.REG_PASSWORD).send_keys("123")
        driver.find_element(*Locators.REG_BUTTON_DATA).click()
        
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators. WRONG_PASSWORD))

    def test_login_main_page(self, driver):
        driver.find_element(*Locators.ENTRANCE_BUTTON).click()
        driver.find_element(*Locators.LOGIN_EMAIL).send_keys(Data.email)
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(Data.password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.MAKE_ORDER))

    def test_login_private_office(self, driver):
        driver.find_element(*Locators.LOGIN_PERSONAL_ACC).click()
        driver.find_element(*Locators.LOGIN_EMAIL).send_keys(Data.email)
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(Data.password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.MAKE_ORDER))

    def test_login_through_registration(self, driver):
        driver.find_element(*Locators.LOGIN_PERSONAL_ACC).click()
        driver.find_element(*Locators.REG_BUTTON).click()
        driver.find_element(*Locators.LOGIN).click()
        driver.find_element(*Locators.LOGIN_EMAIL).send_keys(Data.email)
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(Data.password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.MAKE_ORDER))

    def test_login_through_recover_password(self, driver):
        driver.find_element(*Locators.ENTRANCE_BUTTON).click()
        driver.find_element(*Locators.FORGOT_PASSWORD).click()
        driver.find_element(*Locators.LOGIN).click()
        driver.find_element(*Locators.LOGIN_EMAIL).send_keys(Data.email)
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(Data.password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.MAKE_ORDER))



              





          

    



        

        

        





        







