"""
文件下载
"""
from selenium import webdriver
import os
options =webdriver.ChromeOptions()

prefs = {'profile.default_content_settings.popups' : 0,
         'download.default_directory' : os.getcwd()}
options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome()
driver.get("https://pypi.org/project/selenium/#files")
driver.find_element_by_xpath('//*[@id="files"]/table/tbody/tr[2]/th/a').click()

