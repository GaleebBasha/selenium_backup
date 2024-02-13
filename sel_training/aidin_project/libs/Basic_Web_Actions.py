from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Basic_Act():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")

    def get_url(self, url):
        self.driver.get(url=url)
        # self.driver.get_screenshot_as_file("error1.png")
        if(self.driver.find_element_by_id("txtUsername")):
            print("Reached Web Page Successfully")

    def get_title(self):
        title = self.driver.title
        print("Title is", title)
        assert "OrangeHRM" in title

    def login_with_valid_credentials(self, username, password):
        self.driver.find_element_by_id("txtUsername").send_keys(username)
        self.driver.find_element_by_id("txtPassword").send_keys(password)
        self.driver.find_element_by_id("btnLogin").click()
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, "welcome")))

    def login_with_invalid_credentials(self):
        self.driver.find_element_by_id("txtUsername").send_keys("jhgaksd")
        self.driver.find_element_by_id("txtPassword").send_keys("hgadajh")
        self.driver.find_element_by_id("btnLogin").click()
        data = self.driver.find_element_by_xpath('//span[@id="spanMessage"]').text
        assert data == "Invalid credentials"
