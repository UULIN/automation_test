"""
多窗口切换
current_window_handle：获得当前窗口的句柄
window_handles:返回所有窗口的句柄到当前会话
switch_to.windows()：切换到对应窗口
"""
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")

search_window = driver.current_window_handle
print(driver.title)

driver.find_element_by_css_selector('div#u1 > a[name="tj_login"]').click()
# 此处不加显式等待可能加载不出来
element = WebDriverWait(driver, 3, 0.5).until(
    EC.visibility_of_element_located((By.XPATH,"//a[text() = '立即注册']"))
)
element.click()
all_windows = driver.window_handles

for handle in all_windows:
    if handle != search_window:
        driver.switch_to.window(handle)
        print(driver.title)
        driver.find_element_by_css_selector('[name="userName"]').send_keys("username12343")
        driver.find_element_by_css_selector('[name="phone"]').send_keys("18061257979")
        driver.find_element_by_css_selector('#TANGRAM__PSP_4__password').send_keys("123451236")

        sleep(2)
        driver.close()

driver.switch_to.window(search_window)
print(driver.title)

