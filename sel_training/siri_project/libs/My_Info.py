import time

from Basic_Act import  Basic_Actions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class My_Information(Basic_Actions):
    def navigate_myinfo_page(self):
        self.driver.find_element_by_xpath("//b[contains(text(), 'My Info')]").click()
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//label[contains(text(), 'Full Name')]")))
            return True
        except Exception as e:
            print("My Info Page is Not Seen")
            return False

    def edit_my_info(self):
        time.sleep(3)
        self.driver.find_element_by_id('btnSave').click()
        # time.sleep(3)
        # self.driver.find_element_by_id('personal_txtEmployeeId').clear()
        self.driver.find_element_by_id('personal_txtEmployeeId').send_keys('0001')
        self.driver.find_element_by_id('personal_optGender_1').click()
        time.sleep(1)

        sel = Select(self.driver.find_element_by_id('personal_cmbMarital'))
        sel.select_by_visible_text('Single')
        time.sleep(1)

        self.driver.find_element_by_class_name("ui-datepicker-trigger").click()

        sel = Select(self.driver.find_element_by_class_name('ui-datepicker-year'))
        sel.select_by_visible_text('1994')
        time.sleep(1)
        sel = Select(self.driver.find_element_by_class_name("ui-datepicker-month"))
        sel.select_by_visible_text('Feb')
        time.sleep(1)
        self.driver.find_element_by_xpath("//table[@class='ui-datepicker-calendar']/tbody/tr[5]/td[2]").click()
        time.sleep(5)

        self.driver.find_element_by_id('btnSave').click()
        time.sleep(60)


