from selenium import webdriver
from time import sleep
import unittest
import codecs
import csv
from itertools import islice
from parameterized import parameterized
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


    @parameterized.expand(
        [('case1','selenium'),
         ('case2','unittest'),
         ('case3','parameterized')])
    def test_search(self,name,search_key):
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title, search_key + "_百度搜索")





    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
