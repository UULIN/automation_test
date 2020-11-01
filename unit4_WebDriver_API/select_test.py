from selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()



driver.get("http://www.baidu.com")
driver.maximize_window()
# 打开搜索设置
driver.find_element_by_id('s-usersetting-top').click()


driver.find_element_by_link_text('搜索设置').click()
sleep(1)

# 打开高级搜索

driver.find_element_by_xpath('//*[@id="wrapper"]/div[6]/div/div/ul/li[2]')

sleep(2)
sel = driver.find_element_by_class_name('c-select-selected-value')

Select(sel).select_by_visible_text('最近一天')


sleep(2)


driver.close()