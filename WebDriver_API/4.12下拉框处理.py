"""
下拉框是web的常用功能之一，webdriver提供了select类来处理下拉框
select_by_value() 通过value的值来定位下拉框选项
select_by_visible_text()通过text的值来定位下拉框选项
select_by_index()根据下拉框选项的索引进行选择
"""
from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
sleep(2)

driver.find_element_by_css_selector("#s-usersetting-top").click()
driver.find_element_by_xpath('//*[@id="s-user-setting-menu"]/div/a[2]').click()
sleep(2)

sel = driver.find_element_by_xpath('//*[@id="adv-setting-gpc"]/div/div[1]/span').click()
# Select(sel).select_by_visible_text("最近一天")
# sleep(2)
driver.find_element_by_xpath('//*[@id="adv-setting-gpc"]/div/div[2]/div[2]/p[2]').click()
sleep(2)
