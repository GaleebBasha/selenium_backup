import time

from Basic_Act import Basic_Actions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Admin_Act(Basic_Actions):
    def navigate_admin_page(self):
        self.driver.find_element_by_xpath("(//a[@class='firstLevelMenu'])[1]/b").click()
        try:
            #self.driver.find_element_by_class_name("toggle tiptip").text
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "searchSystemUser_userName")))
            return True
        except Exception as e:
            print("Admin Page is not seen")
            return False

    def delete_record(self, rec_xpath):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, rec_xpath)))
        self.driver.find_element_by_xpath(rec_xpath).click()
        self.driver.find_element_by_id("btnDelete").click()
        # self.driver.switch_to.alert.dismiss()
        self.driver.find_element_by_xpath("(//div[@class='modal-footer'])[2]/input[2]").click()
        time.sleep(3)
