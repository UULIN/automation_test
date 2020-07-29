"""
鼠标相关的操作方法都封装在ActionChains类里面
perform() 执行ActionChains类中存储的所有行为
context_click() 右击
double_click() 双击
drag_and_drop() 拖动
move_to_element() 鼠标悬停
"""
from selenium.webdriver import ActionChains
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/?tn=78000241_hao_pg")

element = driver.find_element_by_css_selector("#s-usersetting-top")
# 对元素执行悬停操作
ActionChains(driver).move_to_element(element).perform()
element1 = driver.find_element_by_xpath("//span[@id='s-usersetting-top']")
# 对元素进行双击操作
ActionChains(driver).double_click(element1).perform()