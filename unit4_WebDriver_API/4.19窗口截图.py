"""
save_screenshot()
"""
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")

driver.save_screenshot("./baidu.img.png")