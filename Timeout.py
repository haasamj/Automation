from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox(executable_path='geckodriver.exe')
browser.get("https://www.facebook.com")
browser.maximize_window()

username = browser.find_element_by_id('email')
password = browser.find_element_by_id('pass')
submit = browser.find_element_by_xpath('//*[@id="u_0_a"]')

username.send_keys('9910407526')
password.send_keys('Si121997')
submit.click()

browser.close()

