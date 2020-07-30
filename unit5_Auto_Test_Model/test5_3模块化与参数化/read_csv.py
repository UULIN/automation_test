"""
读取csv文件
"""
import csv
from itertools import islice
import codecs
import os
# 读取本地csv文件
path = os.path.abspath("config")
data = csv.reader(codecs.open(path+"\\user_info.csv", "r",  encoding="gbk"))

# 存放用户数据
users = []

# 循环输出每行信息
for line in islice(data, 1, None):
    users.append(line)
print(users)
