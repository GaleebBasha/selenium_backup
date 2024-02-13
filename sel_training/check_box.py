from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
#driver.implicitly_wait(10)

# driver.get("https://fs9.formsite.com/VaKMNL/lwjqg5ubbs/index.html?1630034165990")
#
# sel = Select(driver.find_element_by_id("RESULT_RadioButton-0"))
#
# sel.select_by_visible_text('ABS')
# time.sleep(2)
# sel.select_by_value('Radio-2')
# time.sleep(2)
# sel.select_by_index(1)
#
# check_boxes = driver.find_elements_by_xpath("(//table[@class='inline_grid choices']/tbody)[1]/tr")
#
# print(check_boxes)
#
# for c in check_boxes:
#     print("Clicking on ",c.text)
#     if c.text == 'Fish':
#         c.click()
#     time.sleep(2)
#
# time.sleep(5)
#
# driver.find_element_by_xpath("//label[contains(text(), 'Bang')]").click()
#
# driver.find_element_by_id("FSsubmit").click()
#
# time.sleep(5)
# driver.quit()

driver.get("https://fs9.formsite.com/VaKMNL/r874nupsl3/index.html?1630291893806")
elems = driver.find_elements_by_xpath("//table[@class='matrix choices']/tbody/tr/td/label")

print(elems)

nums = driver.find_elements_by_xpath("//table[@class='matrix choices']/tbody/tr/td[1]")

new_num_list = []

for i in nums:
    new_num_list.append(i.text)

print("list ", new_num_list)

for i,k in zip(elems, new_num_list):
    if k == '2' or k == '3':
        print(i.text)
        i.click()

time.sleep(5)