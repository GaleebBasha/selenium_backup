from siri_project.libs.Basic_Act import  Basic_Actions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class My_Directory(Basic_Actions):
    def navigate_to_directory_page(self):
        self.driver.find_element_by_xpath("//b[contains(text(), 'Directory')]").click()
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "searchDirectory_emp_name_empName")))
            return True
        except Exception as e:
            print("Directory Page is not found")
            return False
