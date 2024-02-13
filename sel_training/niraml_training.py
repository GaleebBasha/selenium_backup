from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")

src1 = driver.find_element_by_id("box1")
dest1 = driver.find_element_by_id('box104')

src2 = driver.find_element_by_id('box2')
dest2 = driver.find_element_by_id('box106')

actions = ActionChains(driver)

actions.drag_and_drop(src1, dest1).perform()
actions.drag_and_drop(src2, dest2).perform()
hold = driver.find_element_by_id('box3')
actions.click_and_hold(hold).perform()
time.sleep(5)



