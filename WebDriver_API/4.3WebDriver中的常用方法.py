"""
clear() 清除文本
click() 点击元素
send_keys 模拟按键输入
size 返回元素的大小
text 获取元素的文本
get_attribute 获取元素的属性
is_displayed 设置该元素是否用户可见
"""
from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()

driver.get("https://www.baidu.com/")
# size返回元素的高和宽
size = driver.find_element_by_css_selector(".s_ipt").size

text = driver.find_element_by_css_selector(".s-bottom-layer-right").text

attribute = driver.find_element_by_css_selector(".s_ipt").get_attribute("maxlength")

displayed = driver.find_element_by_css_selector("#su").is_displayed()
print(size, text, attribute, displayed, end=' ')
