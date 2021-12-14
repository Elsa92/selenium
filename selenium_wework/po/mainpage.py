from time import sleep

import allure
from selenium.webdriver.common.by import By

from selenium_wework.po.addresspage import AddressPage
from selenium_wework.po.basepage import BasePage


class MainPage(BasePage):
    _contact_menu = (By.ID, 'menu_contacts')

    @allure.feature('点击通讯录，进入联系人界面')
    def goto_addresspage(self):
        self.find_and_click(*self._contact_menu)
        return AddressPage(self.driver)

