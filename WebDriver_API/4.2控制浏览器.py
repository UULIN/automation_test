from selenium import webdriver
from time import sleep

wb = webdriver.Chrome()

wb.set_window_position(0,0)
wb.set_window_size(600, 600)

first_url = 'https://www.baidu.com'
print("first access %s" % first_url)
wb.get(first_url)

second_url = 'https://www.hao123.com/'
print("second access %s" % second_url)
wb.get(second_url)
sleep(1)
print("back to first: %s" % first_url)
wb.back()
sleep(1)
print("forward to  second: %s" % second_url)
wb.forward()
sleep(1)
print('刷新浏览器')
wb.refresh()
wb.close()