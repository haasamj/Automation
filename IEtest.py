from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Ie(executable_path='IEDriverServer.exe')

driver.get('https://www.google.com')
print(driver.title)
driver.close()

#it's not working