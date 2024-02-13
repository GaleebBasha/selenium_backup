from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import  ActionChains
import time
driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
driver.get("http://testautomationpractice.blogspot.com/")

button = driver.find_element_by_xpath("//button[contains(text(), 'Copy Text')]")
action = ActionChains(driver)

action.double_click(button).click().perform()

time.sleep(5)

