from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
driver.get("http://testautomationpractice.blogspot.com/")

actions = ActionChains(driver)

#actions.drag_and_drop(src1, dest1).perform()
#actions.drag_and_drop(src2, dest2).perform()

button = driver.find_element_by_xpath("//button[contains(text(), 'Copy Text')]")
actions.double_click(button).perform()
time.sleep(5)