from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
#driver.implicitly_wait(10)

driver.get("https://fs9.formsite.com/")
time.sleep(2)
#driver.maximize_window()

driver.find_element_by_xpath("(//div[@class='container']/a)[1]").click()
time.sleep(2)

# driver.find_element_by_xpath("(//a[@class='auth-indicator__link'])[1]").click()
# time.sleep(2)
driver.find_element_by_id('UserId').send_keys("skafrin201.as@gmail.com")

driver.find_element_by_id("Password").send_keys("Afrin@201")
#
driver.find_element_by_id("login").click()

time.sleep(10)

try:
    email_id = driver.find_element_by_id("menu-user-trigger").text
    print(email_id)
except Exception as e:
    raise Exception("Failed to Logon because of {}".format(e))
time.sleep(10)

driver.quit()
