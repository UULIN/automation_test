from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.common.exceptions import UnexpectedAlertPresentException
opt = webdriver.ChromeOptions()
opt.add_experimental_option('w3c',  False)
driver = webdriver.Chrome(chrome_options=opt)


def huadongkuai():
    driver.get("https://www.helloweba.net/demo/2017/unlock/")
    # 定位滑动块
    slider = driver.find_elements_by_css_selector(".slide-to-unlock-handle")[0]
    aciton = ActionChains(driver)
    aciton.click_and_hold(slider).perform()

    for index in range(149):
        try:
            aciton.move_by_offset(index, 0).perform()
        except UnexpectedAlertPresentException:
            break
        # aciton.reset_actions()
        sleep(0.01)
    success = driver.switch_to.alert.text
    print(success)
def huadongdate():
    driver.get("http://www.jq22.com/yanshi4976")
    sleep(2)
    driver.switch_to.frame("iframe")
    driver.find_element_by_css_selector("#appDate").click()
    #定位要滑动的年月日
    element = driver.find_elements_by_css_selector(".dwwo")
    year = element[0]
    mouth = element[1]
    day = element[2]
    action = webdriver.TouchActions(driver)
    action.scroll_from_element(year, 0, 5).perform()
    action.scroll_from_element(mouth, 0, 4).perform()
    action.scroll_from_element(day, 0, 10).perform()
    driver.find_elements_by_css_selector(".dwb")[0].click()


if __name__ == '__main__':
    huadongdate()
