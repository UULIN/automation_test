import unittest


class TestAssert(unittest.TestCase):
    def test_equal(self):
        self.assertEqual(2+2, 4)
        self.assertNotEqual(2,1,msg="not_equal")

    def test_in(self):
        self.assertIn("abbb", "abbbbbbb", msg="yes_in")
        self.assertNotIn("avc", "oijoi", msg="not_in")

    def test_true(self):
        self.assertTrue(True)
        self.assertFalse(False)

if __name__ == '__main__':
    unittest.main()