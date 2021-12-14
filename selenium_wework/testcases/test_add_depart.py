import pytest
from faker import Faker

from selenium_wework.po.mainpage import MainPage


class TestDemo():
    def setup_class(self):
        self.main = MainPage()
        self.faker = Faker('zh-CN')

    def teardown_class(self):
        self.main.close()

    # @pytest.mark.parametrize('name', ['ceshi'])
    def test_logon(self):
        name = self.faker.job()
        text = self.main.goto_addresspage().click_add_icon().input_info(name).get_adddepart_string()
        assert '新建部门成功' == text 