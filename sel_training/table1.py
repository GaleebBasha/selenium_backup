from selenium import webdriver

from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")

driver.get("https://www.careerpower.in/states-and-capitals-of-india.html")

l_col = len(driver.find_elements_by_xpath("(//table[@class='table table-bordered table-striped table-hover'])[1]/thead/tr[2]/th"))

l_row = len(driver.find_elements_by_xpath("(//table[@class='table table-bordered table-striped table-hover'])[1]/tbody/tr"))


print(l_col,l_row)
states_dict = {}
for row in range(1, l_row+1):
    list_tmp = []
    for col in range(1, l_col+1):
        tmp = driver.find_element_by_xpath("(//table[@class='table table-bordered table-striped table-hover'])[1]/tbody/tr[{}]/td[{}]".format(row, col)).text
        list_tmp.append(tmp)
    states_dict.update({list_tmp[0]:list_tmp[1::]})

print(states_dict)
driver.quit()