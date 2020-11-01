from selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.maximize_window()

cookies = driver.get_cookies()

for coookie in cookies:
    print('%s --> %s'% (coookie['name'], coookie['value']))
print(cookies)

driver.close()