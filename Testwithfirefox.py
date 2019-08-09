from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Firefox(executable_path='geckodriver.exe')
driver.maximize_window()

# driver.get('https://www.google.com')
# print(driver.title) #title of the page
# print(driver.current_url) #current url of the page
# print(driver.page_source) #HTML Code for the page
# elem = driver.find_element_by_name('q')
# elem.clear()
# elem.send_keys('Love Images')
# elem = driver.find_element_by_xpath("//div[@class='FPdoLc VlcLAe']//input[@name='btnK']")
# elem.click()
driver.get("http://demo.automationtesting.in/Windows.html")
driver.find_element_by_xpath('//*[@id="Tabbed"]/a/button').click()
time.sleep(10)
driver.quit() #close() is used for one tab(parent tab) and quit() is used for window