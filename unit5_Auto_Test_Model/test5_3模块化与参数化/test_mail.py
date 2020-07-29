from selenium import webdriver
from unit5_Auto_Test_Model.test5_3模块化与参数化.module_test import Mail
from time import sleep
if __name__ == '__main__':

    driver = webdriver.Chrome()
    driver.get("https://www.126.com/")

    method1 = Mail(driver)
    method1.login("feng_er_lin","qq1036190402")

    sleep(5)
    method1.logout()
    driver.close()