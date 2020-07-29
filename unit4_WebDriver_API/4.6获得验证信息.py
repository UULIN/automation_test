"""
获取当前标题
获取url
获取selenium标题
获取url
获取结果条数
"""
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")

first_title = driver.title
print("当前title is %s" % first_title)
sleep(1)
first_url = driver.current_url
print("当前URL is %s" % first_url)
sleep(1)
# 跳转到url
driver.find_element_by_css_selector("#kw").send_keys("selenium")
driver.find_element_by_css_selector("#su").send_keys(Keys.ENTER)
sleep(2)
# 获取第二个标题
second_title = driver.title
print("second title is %s" % second_title)
sleep(1)
# 获取第二个URL
second_url = driver.current_url
print("second URL is %s" % second_url)
sleep(1)
# 找结果数量
text1 = driver.find_element_by_css_selector(".nums_text").text
print("result num is %s " % text1 )
sleep(2)

