import unittest
from time import sleep
from selenium import webdriver
from parameterized import parameterized

class test_baidu(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.base_url = "https://www.baidu.com/"

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def baidu_search(self, search_key):
        self.driver.get(self.base_url)
        self.driver.find_element_by_css_selector("#kw").send_keys(search_key)
        self.driver.find_element_by_css_selector("#su").click()
        sleep(2)
    @parameterized.expand([
        ("case1","selenium"),
        ("case2", "unittest"),
        ("case3", "parameterized")
    ])
    def test_search(self,name,key_word):
        self.baidu_search(key_word)
        self.assertEqual(self.driver.title, key_word+"_百度搜索")

if __name__ == '__main__':
    unittest.main(verbosity=2)
