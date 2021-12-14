from selenium.webdriver.common.by import By

from selenium_wework.po.adddepartpage import AddDepartPage
from selenium_wework.po.basepage import BasePage


class AddressPage(BasePage):
    _add_icon = (By.XPATH, '//*[@class="member_colLeft_cntWrap"]/div/a')
    _add_depart = (By.XPATH, '//*[@class="member_colLeft"]/ul/li/a')
    _departments = (By.XPATH, '//*[@class="jstree jstree-1 jstree-default"]//a')
    _string = (By.ID, 'js_tips')

    def click_add_icon(self):
        self.find_and_click(*self._add_icon)
        self.find_and_click(*self._add_depart)
        return AddDepartPage(self.driver)

    def get_depart_name(self):
        depart_list = []
        eles = self.find_eles(*self._departments)
        for value in eles:
            depart_list.append(value.text)
        return depart_list

    def get_adddepart_string(self):
        ele = self.find_ele(*self._string).text
        return ele
