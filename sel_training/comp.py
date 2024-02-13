from selenium import webdriver

import time



driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")

#driver.get("http://testautomationpractice.blogspot.com/")


#h1 = driver.find_element_by_xpath("//div[@class='segment_header']/h1").text

#print(h1)
#time.sleep(100)
#
# driver.find_element_by_xpath("(//div[@class='widget-content'])[1]/button").click()
#
# time.sleep(2)
#
# driver.switch_to.alert.accept()
#
# driver.find_element_by_xpath("(//div[@class='widget-content'])[1]/button").click()
#
# time.sleep(2)
#
#
# # data_popup = driver.switch_to.alert.text
# #
# # print("The Pop Up Data is {}".format(data_popup))
#
# #driver.find_element_by_xpath("(//div[@class='widget-content'])[6]/button").dou
# # actions = ActionChains(driver)
# # actions.double_click("(//div[@class='widget-content'])[6]/button").perform()
#
#

driver.get("https://www.worldometers.info/geography/flags-of-the-world/")

# scroll down by pixel
#driver.execute_script("window.scrollBy(0, 5000)", "")

# scrolldown to an element
flag = driver.find_element_by_xpath("(//div[@class='row'])[3]/div[37]")
driver.execute_script("arguments[0].scrollIntoView();",flag)
time.sleep(5)


driver.quit()
