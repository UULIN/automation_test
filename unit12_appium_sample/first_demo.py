from appium import webdriver
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
# 定义运行环境
desired_caps = {
    'deviceName':'127.0.0.1:7555',
    'automationName':'appium',
    'platformName': 'Android',
    'platfromVersion':'6.0.1',
    'appPackage':'com.android.browser',
    'appActivity':'.BrowserActivity'

}
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.get("https://m.baidu.com")
sleep(10)
driver.find_element_by_id('index-kw').send_keys("123")
sleep(10)
driver.find_element_by_id("index-bn").click()
driver.quit()