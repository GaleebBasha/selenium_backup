from selenium import webdriver
from selenium.webdriver.common.by import By # to select the locator

from locators.elements import *

class BasicActions():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        
    
    def navigate_url(self):
        self.driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
        
    
    def login(self, user, passwd):
        self.driver.find_element(By.NAME, login['username']).send_keys(user)
        self.driver.find_element(By.NAME, login['password']).send_keys(passwd)
        self.driver.find_element(By.XPATH, login['submit']).click()
        try:
            self.driver.find_element(By.XPATH, login['dashboard'])
            return True
        except Exception:
            msg = self.driver.find_element(By.XPATH, login['error_msg']).text
            print("Error Message:\t",msg)
            return False