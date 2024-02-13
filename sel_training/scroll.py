from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
driver.get("https://www.worldometers.info/geography/flags-of-the-world/")

driver.execute_script("window.scrollBy(0, 5000)", "")

#flag = driver.find_element_by_xpath("(//div[@class='row'])[3]/div[50]")

#driver.execute_script("arguments[0].scrollIntoView();", flag)

time.sleep(10)