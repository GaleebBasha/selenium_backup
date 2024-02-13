from libs.connections import BasicActions
from locators.elements import *
from selenium.webdriver.common.by import By # to select the locator
import time

class MyInfo(BasicActions):
    def navigate_myinfo(self):
        self.driver.find_element(By.XPATH, myinfo['myinfo_tab']).click()
        self.driver.find_element(By.XPATH, myinfo['personal_data'])
    
    def fill_personal_data(self):
        self.driver.find_element(By.XPATH, '//input[@name="firstName"]').clear()
        self.driver.find_element(By.XPATH, '//input[@name="firstName"]').send_keys("xyz")
        self.driver.find_element(By.XPATH, '//input[@name="firstName"]').clear()
        self.driver.find_element(By.XPATH, '//input[@name="middleName"]').clear()
        self.driver.find_element(By.XPATH, '//input[@name="middleName"]').send_keys("pqr")
        self.driver.find_element(By.XPATH, '//input[@name="lastName"]').clear()
        self.driver.find_element(By.XPATH, '//input[@name="lastName"]').send_keys("abc")
        
        self.driver.find_element(By.XPATH, "(//input[@placeholder='yyyy-mm-dd'])[1]").send_keys('1994-12-12')
        self.driver.find_element(By.XPATH, "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[2]").click()
        self.driver.find_element(By.XPATH,'//div[text()="Other"]').click()
        time.sleep(10)
        
        
        
        
        