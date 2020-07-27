"""
cookie主要操作:
get_cookie()返回字典中key为name的cookie
get_cookies()返回所有的cookie
delete_cookie()删除字典中key为name的cookie
delete_all_cookies()删除所有cookies
add_cookie()添加cookie
"""
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")

# 获取所有cookie信息并打印
cookies = driver.get_cookies()

print(cookies)
driver.add_cookie({'name': 'aaaa', 'value': 'bbbb'})
cookies = driver.get_cookies()
print(cookies)
for cookie in cookies:
    print('%s - %s' % (cookie['name'], cookie['value']))