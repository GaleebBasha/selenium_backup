import time

from .Basic_Web_Actions import Basic_Act
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class MyInfo(Basic_Act):
    def navigate_to_my_info_page(self):
        self.driver.find_element_by_xpath('//b[contains(text(), "My Info")]').click()
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, "personal_txtEmpFirstName")))

    def fill_up_personal_details(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id("btnSave").click()
        self.driver.find_element_by_id("personal_txtEmpFirstName").send_keys("Peter")
        self.driver.find_element_by_id("personal_txtEmpMiddleName").send_keys("John")
        self.driver.find_element_by_id("personal_optGender_2").click()
        select = Select(self.driver.p("personal_cmbNation"))
        select.select_by_value("194")

        self.driver.find_element_by_xpath('(//img[@class="ui-datepicker-trigger"])[2]').click()

        select = Select(self.driver.find_element_by_class_name("ui-datepicker-year"))
        select.select_by_value("1930")

        select = Select(self.driver.find_element_by_class_name("ui-datepicker-month"))
        select.select_by_visible_text("Jan")


        self.driver.find_element_by_xpath('(//a[@class="ui-state-default"])[5]').click()

        time.sleep(10)