"""
webDriver的execute——script()方法执行javascript代码
windows.scrollTO()
"""
from time import sleep
from selenium import webdriver
driver = webdriver.Chrome()
driver.set_window_size(800,600)
driver.get("https://www.baidu.com/")


driver.find_element_by_css_selector('#kw').send_keys("selenium")
# driver.find_element_by_css_selector("#su").click()
driver.find_element_by_id("su").click()
# js1 = "window.scrollTo(100,300);"
sleep(2)
js1 = "window.scrollTo(100,450);"

# js1 = "window.scrollTo(100,450);"
driver.execute_script(js1)
