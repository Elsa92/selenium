from time import sleep

from selenium.webdriver.common.by import By


from selenium_wework.po.basepage import BasePage


class AddDepartPage(BasePage):
    _depart_name = (By.XPATH, '//*[@class="member_tag_dialog_inputDlg"]//form/div[1]/input')
    _select_depart = (By.XPATH, '//*[@class="member_tag_dialog_inputDlg"]//form/div[3]/a')
    _depart = (By.XPATH, '//*[@class="qui_dropdownMenu ww_dropdownMenu member_colLeft js_party_list_container"]/div/ul/li/a')
    _confirm_button = (By.XPATH, '//*[@class="qui_dialog_foot ww_dialog_foot"]/a[1]')

    def input_info(self,name):
        from selenium_wework.po.addresspage import AddressPage
        self.find_ele(*self._depart_name).send_keys(name)
        self.find_and_click(*self._select_depart)
        self.find_and_click(*self._depart)
        self.find_and_click(*self._confirm_button)
        # sleep(5)
        return AddressPage(self.driver)
