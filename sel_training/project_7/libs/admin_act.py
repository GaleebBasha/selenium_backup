import time

from .base_act import Basic_Actions
from selenium.webdriver.support.select import Select

class Admin_Actions(Basic_Actions):
    def navigate_to_admin_page(self):
        self.driver.find_element_by_xpath('//b[contains(text(), "Admin")]').click()
        # data = self.driver.find_element_by_xpath("//a[@class='toggle tiptip']").text
        data = self.driver.current_url
        print("text is", data)
        if('viewSystemUsers' in data):
            return True
        else:
            return False

    def search_user(self):
        self.driver.find_element_by_id("searchSystemUser_userName").send_keys("Admin")
        sel = Select(self.driver.find_element_by_id("searchSystemUser_userType"))
        sel.select_by_value("1")
        self.driver.find_element_by_id("searchSystemUser_employeeName_empName").send_keys("naresh palle")
        time.sleep(3)
        sel = Select(self.driver.find_element_by_id("searchSystemUser_status"))
        sel.select_by_visible_text("All")

        self.driver.find_element_by_name("_search").click()

    def delete_user(self):
        self.driver.find_element_by_id("ohrmList_chkSelectRecord_10").click()
        self.driver.find_element_by_name("btnDelete").click()
        self.driver.find_element_by_id("dialogDeleteBtn").click()