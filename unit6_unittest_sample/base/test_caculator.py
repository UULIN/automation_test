import unittest
from unit6_unittest_sample.base.caculator import Caculator


class Test_Caculator(unittest.TestCase):
    def setUp(self) -> None:
        print("start:")

    def tearDown(self) -> None:
        print("end")

    def test_add(self):
        c = Caculator(5, 6)
        result = c.add()
        self.assertEqual(result, 11)

    def test_sub(self):
        c = Caculator(5, 1)
        result = c.sub()
        self.assertEqual(result, 3)

    def test_mul(self):
        c = Caculator(3, 5)
        result = c.mul()
        self.assertEqual(result, 15)

    def test_div(self):
        c = Caculator(6, 3)
        result = c.div()
        self.assertEqual(result, 2)

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Test_Caculator("test_add"))
    suite.addTest(Test_Caculator("test_sub"))
    suite.addTest(Test_Caculator("test_mul"))
    suite.addTest(Test_Caculator("test_div"))

    runner = unittest.TestRunner()
    runner.run(suite)