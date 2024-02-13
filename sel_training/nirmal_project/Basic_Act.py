from selenium import  webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Basic_Actions():
    def __init__(self, executable):
        self.executable = executable
        self.driver = webdriver.Chrome(executable_path=self.executable)

    def get_url(self, url):
        self.url = url
        self.driver.get(self.url)

    def get_title(self, exp_title):
        act_title = self.driver.title
        print("Actual Title is ", act_title)
        if act_title == exp_title:
            return True
        else:
            return False

    def success_login(self, user, pwd):
        self.driver.find_element_by_name('txtUsername').send_keys(user)
        self.driver.find_element_by_name('txtPassword').send_keys(pwd)
        self.driver.find_element_by_name('Submit').click()

        try:
            myElem = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'menu_admin_viewAdminModule')))

        except Exception as e:
            print("Login is unsuccessfully: ", e)
            return False
        return True

    def check_FPWD(self):
        self.driver.find_element_by_link_text('Forgot your password?').click()
        try:
            myElem = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "securityAuthentication_userName")))
            return True
        except Exception as e:
            print("Forget Password Link is not seen", e)
            return False
