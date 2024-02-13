import time

from Basic_Act import Basic_Actions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class My_Information(Basic_Actions):
    def navigate_my_info(self):
        self.driver.find_element_by_xpath("//b[contains(text(), 'My Info')]").click()
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//b[contains(text(), 'My Info')]")))
            self.driver.get_screenshot_as_file('SS/edit123.png')
            return True
        except Exception as e:
            print("My Info Page is not found", e)
            return False
    def edit_personals(self):
        self.driver.execute_script("window.scrollBy(0, 200)", "")
        self.driver.find_element_by_id('btnSave').click()
        print("Het there")
        self.driver.find_element_by_id("personal_txtEmpMiddleName").send_keys("Python")
        self.driver.find_element_by_id("personal_optGender_2").click()
        sel = Select(self.driver.find_element_by_id("personal_cmbMarital"))
        sel.select_by_visible_text("Other")
        self.driver.find_element_by_id("personal_DOB").click()
        sel = Select(self.driver.find_element_by_class_name("ui-datepicker-year"))
        sel.select_by_visible_text("1999")
        sel = Select(self.driver.find_element_by_class_name('ui-datepicker-month'))
        sel.select_by_visible_text('Mar')
        self.driver.find_element_by_xpath("//table[@class='ui-datepicker-calendar']/tbody/tr[3]/td[3]").click()
        opt = self.driver.find_element_by_id('personal_cmbNation').text
        print("Options are, ", opt)
        self.driver.find_element_by_id('btnSave').click()
        time.sleep(2)


