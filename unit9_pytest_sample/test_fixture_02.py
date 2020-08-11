# 功能函数
def multiply(a, b):
    return a * b

class TestMultiply:

    @classmethod
    def setup_class(cls):
        print("setup_class=============")

    @classmethod
    def teardown_class(cls):
        print("teardown_class============")

    def setup_method(module):
        print("setup_module===========================>")


    def teardown_method(module):
        print("teardown_module=======================>")


    # def setup_function(function):
    #     print("setup_function++++++++++++++++++++++>")
    #
    #
    # def teardown_function(function):
    #     print("teardown++++++++++++++++++++++>")


    def setup(self):
        print("setup--------->")


    def teardown(self):
        print("teardown--------->")

    # ===============测试用例
    def test_multiply_3_4(self):
        print("test_multiply_3_4")
        assert multiply(3,4) == 12

    def test_multiply_a_3(self):
        print("test_strings_a_3")
        assert multiply("a",3) == "aaa"