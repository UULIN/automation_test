from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

"""
CSS几种常见的定位方式
.class: 通过class进行定位
#id: 通过id进行定位
*：选择所有元素
element：选择所有的标签元素
element1 > element2：选择父元素为e1的所有e2元素
element + element: div + input  选择div后面的所有input元素
[attribute=value]:[target="_blank"] 选择target="_blank"的所有元素
"""
driver.get("https://www.baidu.com/")
driver.find_element_by_css_selector(".s_ipt").send_keys('1231')

driver.find_element_by_css_selector('#kw').send_keys('1333')

driver.find_element_by_css_selector('input').send_keys('2222')
driver.find_element_by_css_selector('span > input').send_keys('2222')
# 可以进行各种组合以精准定位
driver.find_element_by_css_selector("form.fm > span > input.s_ipt").send_keys("组合定位")
driver.find_element_by_css_selector("form#form > span > input.s_ipt").send_keys("组合")
# 查找class以s_ip开头的元素
driver.find_element(By.CSS_SELECTOR, "[class^=s_ip]").send_keys("111")
