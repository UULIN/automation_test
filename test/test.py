from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

driver.get("https://www.baidu.com/")
# driver.find_element_by_css_selector("[class='s_ipt']").send_keys('通过元素定位')
# driver.find_element_by_css_selector("[value='百度一下']").click()
# driver.find_element_by_css_selector("form.fm > span > input.s_ipt").send_keys("组合定位")
# driver.find_element_by_css_selector("form#form > span > input.s_ipt").send_keys("组合")
driver.find_element(By.CSS_SELECTOR, "[class^=s_ip]").send_keys("111")
sleep(2)
