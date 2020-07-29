"""
web应用中经常会碰见frame/iframe表单嵌套页面的应用，webdriver只能在一个页面对元素进行识别和定位，无法直接定位frame里面的元素，。
所以需要使用switch_to.frame()方法将当前定位的主体切换为frame表单的内嵌界面
"""
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://email.163.com/")
driver.implicitly_wait(2)

login_iframe = driver.find_element_by_css_selector('iframe[id^="x-URS-iframe"]')
driver.switch_to.frame(login_iframe)
driver.find_element_by_css_selector('[name=email]').send_keys("username")
driver.find_element_by_css_selector('[name=password]').send_keys("password")
driver.find_element_by_css_selector('#dologin').click()
driver.switch_to.default_content()

