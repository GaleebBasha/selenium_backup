from Basic_Act import Basic_Action
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class DashBoard(Basic_Action):
    def assign_leave(self):
        self.driver.find_element_by_link_text('Assign Leave').click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'assign-leave')))
        self.driver.find_element_by_id('assignleave_txtEmployee_empName').send_keys('Ravi')

        type = Select(self.driver.find_element_by_id('assignleave_txtLeaveType'))
        type.select_by_visible_text('US - FMLA')

        self.driver.find_element_by_xpath("(//img[@class='ui-datepicker-trigger'])[1]").click()

        year = Select(self.driver.find_element_by_class_name('ui-datepicker-year'))
        year.select_by_visible_text('2021')

        month = Select(self.driver.find_element_by_class_name('ui-datepicker-month'))
        month.select_by_visible_text('Sep')
        self.driver.find_element_by_xpath("//table[@class='ui-datepicker-calendar']/tbody/tr[5]/td[3]").click()

        self.driver.find_element_by_xpath("(//img[@class='ui-datepicker-trigger'])[2]").click()
        year = Select(self.driver.find_element_by_class_name('ui-datepicker-year'))
        year.select_by_visible_text('2021')

        month = Select(self.driver.find_element_by_class_name('ui-datepicker-month'))
        month.select_by_visible_text('Sep')
        self.driver.find_element_by_xpath("//table[@class='ui-datepicker-calendar']/tbody/tr[5]/td[4]").click()

        self.driver.find_element_by_id('assignleave_txtComment').send_keys("Need to attend cousins Marriage")
        self.driver.find_element_by_id('assignBtn').click()









