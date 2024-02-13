# import webbrowser
import sys

from selenium import webdriver
sys.path.append("../")
from project_7.locators.elems_locs import LOCATORS
class Basic_Actions():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=LOCATORS['exec_path'])

    def get_to_url(self, url):
        self.driver.get(url)

    def valid_login(self, user, passwd):
        self.driver.find_element_by_id(LOCATORS['user_id']).send_keys(user)
        self.driver.find_element_by_id(LOCATORS['pwd_id']).send_keys(passwd)
        self.driver.find_element_by_name(LOCATORS['login_id']).click()

    def verify_login(self):
        try:
            self.driver.find_element_by_xpath('//a[contains(@href, "http://www.orangehrm.com/")]')
            print("Login is Successful")
            return True
        except Exception:
            print("Login was unsuccessful")
            return False

