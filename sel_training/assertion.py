import unittest
from selenium import webdriver


class Test(unittest.TestCase):
    def testTitle(self):
        driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
        driver.get("https://www.google.com/")
        title = driver.title
        self.assertEqual('Google', title, 'Title is not same')
        driver.get_screenshot_as_file("title.png")
        driver.quit()

    def testFPW(self):
        driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
        driver.get("https://opensource-demo.orangehrmlive.com/")
        data=driver.find_element_by_xpath("//a[contains(text(), 'Forgot your password?')]").text
        print(data)
        driver.get_screenshot_as_file('FPWD.png')
        driver.quit()


if __name__ == '__main__':
    unittest.main()