from selenium import webdriver
from time import sleep
import unittest
import codecs
import csv
from itertools import islice


class Test_baidu(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.base_url = 'http://www.baidu.com'
        cls.source_list = []
        with codecs.open('baidudata.csv', 'r', 'utf_8_sig') as f:
            keydata = csv.reader(f)
            for line in islice(keydata, 1, None):
                cls.source_list.append(line)


    def baidu_search(self, search_key):
        self.driver.get(self.base_url)
        self.driver.find_element_by_name('wd').send_keys(search_key)
        self.driver.find_element_by_id('su').click()
        sleep(2)
        # pass

    def test_search_selenium(self):
        self.baidu_search(self.source_list[0][1])

    def test_search_unittest(self):
        self.baidu_search(self.source_list[1][1])


    def test_search(self):
        pass


    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
