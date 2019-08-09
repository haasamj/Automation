from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get('http://www.python.org')

a = []
a = driver.find_elements_by_tag_name('a')
print(a)
print(len(a))