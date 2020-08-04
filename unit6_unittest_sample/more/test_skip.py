"""
测试跳过某些测试用例
unittest.skip(reason) 无条件的跳过装饰器的测试，需要标明跳过的原因
unittest.skipIF(condition, reason) 如果条件为真，则跳过装饰器的测试
unittest.skipUnless(condition, reason) 当条件为真时，执行装饰器的测试
unittest.expectedFailure() 不管执行是否失败，都将测试标记为失败
"""
import unittest


class My_test(unittest.TestCase):
    @unittest.skip("测试无条件跳过测试用例")
    def test_skip(self):
        print("aaa")

    @unittest.skipIf(3>2,"测试当条件为真时，跳过测试用例")
    def test_skipif(self):
        print("bbb")

    @unittest.skipUnless(3>2, "测试当条件为真时，执行测试用例")
    def test_skipunless(self):
        print("ccc")

    # 不管执行是否失败，直接标记为失败
    @unittest.expectedFailure
    def test_expectedfailure(self):
        self.assertEqual(2, 3)

        
if __name__ == '__main__':
    unittest.main()