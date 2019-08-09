from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://www.facebook.com')

elem = driver.find_element_by_id('email')
elem.clear()
elem.send_keys('9910407526')
elem = driver.find_element_by_id('pass')
elem.clear()
elem.send_keys('Si12199728@@')
a = driver.find_element_by_xpath("//input[@id='u_0_2']")
a.click()