import csv
import codecs
import unittest
from time import sleep
from itertools import islice
from selenium import webdriver

class test_baidu(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.base_url = "https://www.baidu.com/"
        cls.search_list = []
        with codecs.open('baidu_data.csv','r','utf-8') as f:
            data = csv.reader(f)
            for line in islice(data,1,None):
                cls.search_list.append(line)
    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def baidu_search(self, search_key):
        self.driver.get(self.base_url)
        self.driver.find_element_by_css_selector("#kw").send_keys(search_key)
        self.driver.find_element_by_css_selector("#su").click()
        sleep(3)

    def test_selenium(self):
        self.baidu_search(self.search_list[0][1])

    def test_unittest(self):
        self.baidu_search(self.search_list[1][1])

    def test_par(self):
        self.baidu_search(self.search_list[2][1])


if __name__ == '__main__':
    unittest.main(verbosity=2)
