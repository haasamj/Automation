from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.driver.get('https://www.facebook.com')
        self.driver.maximize_window()

    def test_login(self):
        driver = self.driver
        facebookUsername = '9910407526'
        facebookPassword = 'Si12199728@@'

        emailFieldID = 'email'
        passFieldID = 'pass'
        loginButtonXpath = '//input[@value="Log In"]'
        fbLogoXpath = '(//a[contains(@href,"logo")])[1]'

        emailFieldElement = driver.find_element_by_id(emailFieldID)
        passFieldElement = driver.find_element_by_id(passFieldID)
        loginButtonElement = driver.find_element_by_xpath(loginButtonXpath)
        emailFieldElement.clear()
        emailFieldElement.send_keys(facebookUsername)
        passFieldElement.clear()
        passFieldElement.send_keys(facebookPassword)
        loginButtonElement.click()
        driver.find_element_by_xpath(fbLogoXpath)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()