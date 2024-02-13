import time

from Basic_Act import Basic_Action
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class My_Information(Basic_Action):
    def navigate_to_myinfo(self):
        self.driver.find_element_by_xpath("//b[contains(text(), 'My Info')]").click()
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//label[contains(text(), 'Full Name')]")))
            self.driver.get_screenshot_as_file('info.png')
            return True
        except Exception as e:
            print("My Info Page is not displayed")
            return False
    def validate_FPW_link(self):
        self.driver.find_element_by_link_text("Forgot your password?").click()
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'securityAuthentication_userName')))
            return True
        except Exception as e:
            print("Password reset page is not found")
            return False
    def edit_info(self):
        self.driver.find_element_by_id('btnSave').click()
        time.sleep(1)
        options = self.driver.find_element_by_id('personal_cmbNation').text
        print("Printing Options", options, type(options))
        self.driver.find_element_by_id('personal_txtEmpMiddleName').send_keys('Python')
        self.driver.find_element_by_id('personal_optGender_1').click()

        opt = Select(self.driver.find_element_by_id('personal_cmbNation'))
        opt.select_by_visible_text('Indian')

        self.driver.find_element_by_class_name('ui-datepicker-trigger').click()

        opt = Select(self.driver.find_element_by_class_name('ui-datepicker-year'))
        opt.select_by_visible_text("1994")

        opt = Select(self.driver.find_element_by_class_name('ui-datepicker-month'))
        opt.select_by_visible_text('Mar')

        time.sleep(5)
        self.driver.get_screenshot_as_file('edit.png')

        self.driver.find_element_by_id('btnSave').click()
