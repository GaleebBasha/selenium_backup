from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Basic_Action():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
    def get_url(self, url):
        self.driver.get(url)
    def check_title(self, expected_title):
        act_title = self.driver.title
        if act_title == expected_title:
            return True
        else:
            return False
    def success_login(self, user, pwd):
        self.driver.find_element_by_id("txtUsername").send_keys(user)
        self.driver.find_element_by_id('txtPassword').send_keys(pwd)
        self.driver.find_element_by_name('Submit').click()
        try:
            self.driver.find_element_by_id("menu_admin_viewAdminModule").text
            return True
        except Exception as e:
            print("Home Page is not seen :: Failed To Login")
            return False
    def validate_FPW_link(self):
        self.driver.find_element_by_link_text("Forgot your password?").click()
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "securityAuthentication_userName")))
            return True
            # self.driver.find_element_by_id("securityAuthentication_userName").text

        except Exception as e:
            print("Reset password page is not found")
            return False