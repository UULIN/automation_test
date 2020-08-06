import unittest
from selenium import webdriver
from ddt import ddt,data,unpack
from time import sleep

@ddt
class Test_baidu(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.base_url = "https://www.baidu.com/"


    # 编写驱动方法
    def baidu_search(self, keyword):
        self.driver.get(self.base_url)
        self.driver.find_element_by_css_selector("#kw").send_keys(keyword)
        self.driver.find_element_by_css_selector("#su").click()
        sleep(1)

    @data(["case1", "selenium"], ["case2", "unittest"], ["case3", "ddt"])
    @unpack
    def test_baidu_ddt1(self, case, keyword):
        print("test one:", case)
        self.baidu_search(keyword)
        self.assertEqual(self.driver.title,keyword+"_百度搜索")

    @data(("case1", "selenium"),("case2", "unittest"), ("case3", "ddt"))
    @unpack
    def test_baidu_ddt2(self, case, keyword):
        print("test two", case)
        self.baidu_search(keyword)
        self.assertEqual(self.driver.title, keyword+"_百度搜索")

    @data({"keyword": "selenium"}, {"keyword": "unittest"}, {"keyword": "ddt"})
    @unpack
    def test_baidu_ddt3(self, keyword):
        print("test three",keyword)
        self.baidu_search(keyword)
        self.assertEqual(self.driver.title, keyword+"_百度搜索")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)


