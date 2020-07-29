"""
JS内置对象arguments，其包含了函数调用的参数数组,[0]表示取对象的第1个值
currentSrc返回当前音频/视频的URL,如果未设置音频/视频，则返回空字符串
load(),play(),pause()控制视频的加载、播放和暂停
"""
from time import sleep
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://videojs.com/")


video = driver.find_element_by_css_selector("#preview-player_html5_api")

# 返回播放文件地址
url = driver.execute_script("return arguments[0].currentSrc;", video)
print(url)

# 播放视频
print("start")
driver.execute_script("arguments[0].play()", video)

# sleep
sleep(15)

print("stop")
driver.execute_script("arguments[0].pause()",video)


