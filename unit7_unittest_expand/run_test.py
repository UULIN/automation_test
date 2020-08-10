import unittest
import time
import yagmail
from unit7_unittest_expand.test_report.HTMLTestRunner import HTMLTestRunner




def send_mail(report):
    yag = yagmail.SMTP(user="feng_er_lin@126.com",password="NHDSUDADYBYOEEYF", host="smtp.126.com")
    subject = "主题，自动化测试报告"
    contents = "正文，请查看附件"
    yag.send("feng_er_lin@126.com", subject, contents, report)
    print("email has send out")


if __name__ == "__main__":
    # 定义测试用例的目录为当前目录下的test_case目录
    test_dir = "./test_case"
    suit = unittest.defaultTestLoader.discover(test_dir, pattern="test_baidu_ddt.py")
    # 自定义时间戳
    now_time = time.strftime("%Y-%m-%d %H_%M_%S")

    html_report ="./test_report/"+now_time+"result.html"
    # 生成html测试报告
    fp = open(html_report,"wb")
    runner = HTMLTestRunner(stream=fp,title="百度测试报告",description="运行环境：win10")
    runner.run(suit)
    fp.close()
    send_mail(html_report)