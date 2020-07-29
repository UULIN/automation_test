"""
实现两个方法：
login(username, password)
logout()
"""


class Mail:
    def __init__(self, driver):
        self.driver = driver

    """
    实现login方法
    """
    def login(self, username, password):
        """
        :param username:输入用户名
        :param password: 输入密码
        :return: 返回登录状态
        """
        self.driver.switch_to.frame(self.driver.find_element_by_css_selector("[id^='x-URS-iframe']"))
        self.driver.find_element_by_css_selector("[name='email']").clear()
        self.driver.find_element_by_css_selector("[name='email']").send_keys(username)
        self.driver.find_element_by_css_selector('[name="password"]').clear()
        self.driver.find_element_by_css_selector('[name="password"]').send_keys(password)
        self.driver.find_element_by_css_selector('#dologin').click()



    def logout(self):
        """
        :return:退出是否成功
        """
        self.driver.find_element_by_css_selector("#_mail_icon_0_0").click()
        self.driver.find_element_by_css_selector("#_mail_component_72_72").click()