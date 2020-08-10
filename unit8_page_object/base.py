import time


class BasePage:
    """
    基础的page层，封装一些常用的方法
    """
    def __init__(self, driver):
        self.driver = driver

    # 打开页面
    def open(self, url=None):
        if url is None:
            self.driver.get(self.url)
        else:
            self.driver.get(url)

    # id定位
    def by_id(self, _id):
        return self.driver.find_element_by_id(_id)

    # name定位
    def by_name(self, _name):
        return self.driver.find_element_by_name(_name)

    # class定位
    def by_class(self, _class_name):
        return self.driver.find_element_by_classname(_class_name)

    # Xpath定位
    def by_xpath(self, _xpath):
        return self.driver.find_element_by_xpath(_xpath)

    # CSS定位
    def by_css(self, _css):
        return self.driver.find_element_by_css_selector(_css)

    # 获取title
    def get_title(self):
        return self.driver.title

    # 获取页面text，使用CSS选择器定位
    def get_text(self, _css_selector):
        return self.by_css(_css_selector).text

    # 执行JavaScript脚本
    def js(self, _script):
        self.driver.execute_script(_script)

