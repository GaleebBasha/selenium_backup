from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
driver.get("https://opensource-demo.orangehrmlive.com/")

driver.find_element_by_xpath("//input[@name='txtUsername']").send_keys("admin")
time.sleep(2)
driver.find_element_by_xpath("//input[@name='txtPassword']").send_keys("admin123")
time.sleep(2)
driver.find_element_by_xpath("//input[@name='Submit']").click()
time.sleep(10)



#time.sleep(5)
# Mouse Actions/
# - Mouse Hover
# - Double Click
# - Right Click
# - Drag and Drop

admin = driver.find_element_by_xpath("(//a[@class='firstLevelMenu'])[1]/b")
mgmt = driver.find_element_by_xpath("(//a[@class='arrow'])[1]")
users = driver.find_element_by_xpath("(//a[@id='menu_admin_viewSystemUsers'])")


actions = ActionChains(driver)
actions.move_to_element(admin).move_to_element(mgmt).move_to_element(users).click().perform()
time.sleep(10)

