"""
在web_driver处理JavaScript的alert。confirm，prompt非常简单，具体做法是：
1、首先使用switch_to.alert()定位，然后使用
text返回 alert/confirm/prompt中文字的信息
accept()接收现有的警告窗
dismiss()解散现有的警告窗
send_keys()输入文本
"""
from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")

driver.find_element_by_css_selector("#s-usersetting-top").click()
driver.find_element_by_css_selector(".setpref").click()

sleep(2)
driver.find_element_by_css_selector("div#se-setting-7 > a[class^='prefpanelgo']").click()
alert = driver.switch_to.alert
alert_text = alert.text

print(alert_text)
alert.accept()
sleep(2)
driver.close()