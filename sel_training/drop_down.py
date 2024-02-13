from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")

driver.get("https://fs9.formsite.com/VaKMNL/ejvfur81km/index.html?1631584056980")

sel = Select(driver.find_element_by_class_name('drop_down'))

sel.select_by_visible_text('USA')
time.sleep(2)
sel.select_by_value("Radio-3")
time.sleep(2)
sel.select_by_index(1)
time.sleep(4)
driver.find_element_by_name('Submit').click()

time.sleep(5)

driver.quit()