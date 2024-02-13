from selenium import webdriver
import unittest


class Check(unittest.TestCase):
    def testTitle(self):
        driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
        driver.get("https://opensource-demo.orangehrmlive.com/")
        heading = driver.title
        print("******** Heading is {}".format(heading))
        self.assertNotEqual('OrangeHRM', heading, "Titles are unmatched")
        driver.get_screenshot_as_file('title1.png')
        driver.quit()

    def testFPW(self):
        driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
        driver.get("https://opensource-demo.orangehrmlive.com/")
        data = driver.find_element_by_xpath("//div[@id='forgotPasswordLink']/a").text
        print("Data from webpage ", data)
        self.assertEqual("Forgot your password?", data, "Forget Password Link Is Not Implemented Yet!!")

if __name__ == '__main__':
    unittest.main()