from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()

"""
通过xpath来定位
"""

driver.get("https://www.baidu.com/")
# 通过xpath进行定位，相对路径格式为//input[@id='kw'],//input[@name='wd'],//*等等
driver.find_element_by_xpath('//*[@id="kw"]').send_keys('相对路径')
# 绝对路径
driver.find_element_by_xpath('/html/body/div/div[2]/div[5]/div[1]/div/form/span[2]/input').click()
sleep(2)

driver.get("https://www.baidu.com/")
# 层级与属性的结合
driver.find_element_by_xpath("//span[@id='s_kw_wrap']/input").send_keys('找上级元素')
sleep(2)

driver.get("https://www.baidu.com/")
# 使用逻辑运算符
driver.find_element_by_xpath("//input[@class='s_ipt' and @name='wd']").send_keys('使用逻辑运算符')
sleep(2)

driver.get("https://www.baidu.com/")
driver.find_element_by_xpath("//span[contains(@class='s_ipt_wr')]/input").send_keys('使用contains方法')
sleep(2)

driver.get("https://www.baidu.com/")
# 使用contains匹配一个属性中包含的字符串，注意使用contains后面的@class要用，
driver.find_element_by_xpath("//span[contains(@class, 's_ipt_wr')]/input").send_keys('使用contains方法')
sleep(2)

driver.get("https://www.baidu.com/")
# text()= 方法，相当于driver.find_element_by_link_text
# driver.find_element_by_xpath("//a[text()='新闻']").click()
# 相当于部分元素定位,driver.find_element_by_partial_link_text('新').click()
driver.find_element_by_xpath("//a=[contains(text()='新')]").click()
sleep(2)

