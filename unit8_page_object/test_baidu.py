import unittest
from selenium import webdriver
from time import sleep
from unit8_page_object.baidu_page import BaiduPage

class TestBaidu(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()

    def test_baidu_search_case(self):
        page = BaiduPage(self.driver)
        page.open()
        page.search_input("page_object")
        sleep(3)
        page.search_button()
        sleep(2)
        self.assertEqual(page.get_title(),"page_object_百度搜索")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
