import json

import allure
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:

    @allure.feature('使用复用浏览器进入企业微信首页')
    def __init__(self, driver_base:WebDriver=None):
        if driver_base is None:
            # 复用浏览器， 获取cookies， 并将cookies写入 cookies.txt文件里
            opt = webdriver.ChromeOptions()
            opt.debugger_address = '127.0.0.1:9222'
            self.driver = webdriver.Chrome(options=opt)
            self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
            # with open('cookies.json', 'w', encoding='utf-8') as f:
                # f.write(json.dumps(self.driver.get_cookies()))
            with open('../cookies.txt', 'w', encoding='utf-8') as f:
                f.write(json.dumps(self.driver.get_cookies()))
            # 读取cookies.txt文件里边的cookies，并使用cookies登录
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(5)
            self.driver.delete_all_cookies()
            self.driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx')
            with open ('../cookies.txt', 'rb') as f:
                cookies = json.load(f)
                for cookie in cookies:
                    self.driver.add_cookie(cookie)
        else:
            self.driver = driver_base
    # 定义find element 方法
    def find_ele(self,by,locator):
        ele = self.driver.find_element(by, locator)
        return ele

    #定义find elements 方法
    def find_eles(self, by, locator):
        eles = self.driver.find_elements(by, locator)
        return eles

    # 定义find element and click element 方法
    def find_and_click(self,by, locator):
        ele = self.find_ele(by, locator)
        ele.click()

    # 定义close浏览器的方法
    def close(self):
        self.driver.close()

    # 定义截图的方法
    def get_screenshot(self):
        screen = self.driver.get_screenshot_as_png()
        return screen


