import os

import pytest

if __name__ == '__main__':
    pytest.main(['./testcases/test_add_depart.py','--alluredir','./allure-results'])
    os.system('allure serve ./allure-results -o ./report --clean')