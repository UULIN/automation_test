"""
显式等待就是等待某个条件成立则继续执行，否则在打到最大时长时抛出异常（TimeoutException）
"""
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
"""
webdriverwait方法一般与until()和until_not()方法配合使用
until提供的驱动程序作为一个参数，直到返回值为True
until_not直到返回值为False
"""

element = WebDriverWait(driver, 5, 0.5).until(
    EC.visibility_of_element_located((By.ID, "kw2")), message="time out"
)

element.send_keys("selenium")


