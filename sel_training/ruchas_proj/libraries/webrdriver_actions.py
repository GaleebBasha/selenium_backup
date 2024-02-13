import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from configs.locators import loc


class WebActions():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
    
    def launch_website(self, url):
        self.driver.get(url)
    
    def verify_user_creds(self, user, passwd):
        self.driver.find_element(By.NAME, loc["username"]).send_keys(user)
        self.driver.find_element(By.NAME, loc["password"]).send_keys(passwd)
        self.driver.find_element(By.XPATH,loc['login_btn']).click()
        
        try:
            self.driver.find_element(By.XPATH, loc['myinfo_link'])
            return 1
        except:
            print("Invalid Creds")
            return -1