from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")

# driver._switch_to.frame("packageListFrame")
# driver.find_element_by_link_text("org.openqa.selenium").click()
# time.sleep(5)
#
# driver.switch_to.parent_frame()
#
# driver.switch_to.frame("packageFrame")
# time.sleep(5)
# driver.find_element_by_link_text("Alert").click()
# time.sleep(5)
# driver.switch_to.default_content()
#
driver.switch_to.frame("classFrame")
time.sleep(5)
driver.find_element_by_xpath("(//ul[@class='navList']/li[2])[1]").click()