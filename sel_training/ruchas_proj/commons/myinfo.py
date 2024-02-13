from libraries.webrdriver_actions import WebActions
from selenium.webdriver.common.by import By
import time

class MyInfo(WebActions):
    def login(self):
        self.launch_website("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.verify_user_creds("Admin", 'admin123')
        
    def navigate_to_myinfo_page(self):
        self.driver.find_element(By.XPATH, '//a[@href="/web/index.php/pim/viewMyDetails"]').click()
        try:
            self.driver.find_element(By.XPATH, "//h6[normalize-space()='Personal Details']")
        except:
            print("My Info Page Is Not Loaded")
    def edit_myinfo_details(self):
        self.driver.find_element(By.NAME,"firstName").clear()
        self.driver.find_element(By.NAME,"firstName").send_keys("ABC")
        
        self.driver.find_element(By.NAME,"middleName").clear()
        self.driver.find_element(By.NAME,"middleName").send_keys("XYZ")
        
        self.driver.find_element(By.XPATH, '(//div[@class="oxd-select-wrapper"])[2]/div/div').click()
        self.driver.find_element(By.XPATH, '(//div[@class="oxd-select-wrapper"])[2]/div/div').send_keys("single")
        self.driver.find_element(By.XPATH, '//div[contains(text(),"Single")]').click()
        
        self.driver.find_element(By.XPATH,'(//button[@type="submit"])[1]').click()
        time.sleep(5)