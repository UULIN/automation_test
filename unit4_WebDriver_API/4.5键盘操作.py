"""
调用selenium.webdirver.common.keys方法，获取键盘操作
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
element = driver.find_element_by_css_selector("#kw")
element.send_keys("seleniumm")
sleep(1)
element.send_keys(Keys.BACK_SPACE)
sleep(1)
element.send_keys(Keys.SPACE,'教程')
sleep(1)
element.send_keys(Keys.LEFT_CONTROL,'a')
sleep(1)
element.send_keys(Keys.LEFT_CONTROL,'x')
sleep(1)
element.send_keys(Keys.LEFT_CONTROL,'v')
sleep(1)
element.send_keys(Keys.ENTER)
