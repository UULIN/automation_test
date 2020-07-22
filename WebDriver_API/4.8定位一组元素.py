"""
定位一组元素并显示输出
"""
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.baidu.com/")

driver.find_element_by_css_selector("#kw").send_keys("selenium")
driver.find_element_by_css_selector("#su").click()
driver.implicitly_wait(1)

# 定位一组元素
texts = driver.find_elements_by_css_selector("div[tpl='se_com_default'] > h3 > a")

print(len(texts))

for t in texts:
    print(t.text)
driver.quit()