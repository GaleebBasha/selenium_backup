import unittest
from selenium import  webdriver

driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
driver.get("https://opensource-demo.orangehrmlive.com/")
title = driver.title
unittest.TestCase.assertEqual(unittest, title, "Tiles Not Matched")