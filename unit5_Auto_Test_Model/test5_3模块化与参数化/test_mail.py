from selenium import webdriver
from unit5_Auto_Test_Model.test5_3模块化与参数化.module_test import Mail
from time import sleep
import os
# 打印配置目录的绝对路径
path = os.path.abspath("config")


# 读取txt文件配置
def read_txt():
    # 读取配置目录文件
    with open(path+'\\user_info.txt', "r") as user_file:
        data = user_file.readlines()

    user_list = []
    # 对配置信息进行遍历
    for user in data:
        user_list.append(user[:-1].split(":"))
    return user_list


def read_csv():
    pass


def login_method(username, password):

    driver = webdriver.Chrome()
    driver.get("https://www.126.com/")

    method1 = Mail(driver)
    method1.login(username, password)

    sleep(5)
    method1.logout()
    driver.close()


if __name__ == '__main__':
    login_method(read_txt()[0][0],read_txt()[0][1])
    # login_method(user_lis+t[1][0],user_list[1][1])

