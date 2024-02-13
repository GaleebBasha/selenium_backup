
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')

driver.get("https://www.careerpower.in/states-and-capitals-of-india.html")
time.sleep(5)
col_count = len(driver.find_elements_by_xpath("(//table[@class='table table-bordered table-striped table-hover'])[1]/thead/tr[2]/th"))
print("Coloumn Length is ", col_count)

row_count = len(driver.find_elements_by_xpath("(//table[@class='table table-bordered table-striped table-hover'])[1]/tbody/tr"))

print("Row Length is ", row_count)

data_dict = {}

for row in range(1, row_count+1):
    list_data = []
    for col in range(1, col_count+1):
        tmp = driver.find_element_by_xpath("(//table[@class='table table-bordered table-striped table-hover'])[1]/tbody/tr[{}]/td[{}]".format(row, col)).text
        # print("Cell Data, ", tmp)
        list_data.append(tmp)
    data_dict[list_data[0]] = list_data[1:]

print(data_dict)
driver.quit()
