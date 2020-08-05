import unittest
import time
from unit7_unittest_expand.test_report.HTMLTestRunner import HTMLTestRunner

# 定义测试用例的目录为当前目录下的test_case目录
test_dir = "./test_case"
suit = unittest.defaultTestLoader.discover(test_dir,pattern="test*.py")

if __name__ == "__main__":
    # 自定义时间戳
    now_time = time.strftime("%Y-%m-%d %H_%M_%S")


    # 生成html测试报告
    fp = open("./test_report/"+now_time+"result.html","wb")
    runner = HTMLTestRunner(stream=fp,title="百度测试报告",description="运行环境：win10")
    runner.run(suit)
    fp.close()