import unittest
from selenium import webdriver
from time import sleep

class test_baidu(unittest.TestCase):
    """测试百度搜索"""
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.base_url = "https://www.baidu.com/"

    def baidu_search(self,keywords):
        self.driver.get(self.base_url)
        self.driver.find_element_by_css_selector("#kw").send_keys(keywords)
        self.driver.find_element_by_css_selector("#su").click()
        sleep(2)

    def test_search_selenium(self):
        """测试关键字：selenium"""
        search_key = "selenium"
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title,search_key+"_百度搜索")

    def test_search_unittest(self):
        """测试关键字：unittest"""
        search_key = "unittest"
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title,search_key+"_百度搜索")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
if __name__ == '__main__':
    unittest.main()
