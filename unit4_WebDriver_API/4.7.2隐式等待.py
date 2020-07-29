from time import ctime
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
"""
隐式等待是全局变量寻找元素
"""
driver = webdriver.Chrome()

# 设置隐式等待
driver.implicitly_wait(5)
driver.get("https://www.baidu.com/")

try:
    print(ctime())
    driver.find_element_by_css_selector("#kw1").send_keys("selenium")
except NoSuchElementException as e:
    print("定位失败",e)
finally:
    print(ctime())
    driver.quit()