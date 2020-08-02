"""
读取json
"""
import json
import os
path = os.path.abspath("config")

with open(path+"\\user_info.json", "r") as f:
    data = f.read()
userlist = json.loads(data)
print(userlist)