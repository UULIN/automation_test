from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
"""
元素定位
"""
driver.get("https://www.baidu.com/")
# 通过元素的id进行定位
driver.find_element_by_id('kw').send_keys('selenium')
sleep(2)
driver.find_element_by_id('su').click()

driver.get("https://www.baidu.com/")
# 通过元素的name进行定位
driver.find_element_by_name('wd').send_keys('byname')
sleep(2)

driver.get("https://www.baidu.com/")
# 通过元素的classname进行定位
driver.find_element_by_class_name('s_ipt').send_keys('s_ipt')
sleep(2)

driver.get("https://www.baidu.com/")
# 通过元素的标签进行定位，但是元素的标签往往有多个，一般会定位失败
#driver.find_element_by_tag_name('input').send_keys('tagname')

driver.get("https://www.baidu.com/")
# 通过元素的文本连接来定位
driver.find_element_by_link_text('新闻').click()
sleep(2)

driver.get("https://www.baidu.com/")
# 是对by_link的一种补充，如果文字的链接比较长，可以输入部分文字进行定位
driver.find_element_by_partial_link_text('新').click()
sleep(2)






driver.close()


