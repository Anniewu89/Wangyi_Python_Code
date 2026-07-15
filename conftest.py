import random

import pytest
# from selenium import webdriver
# from selenium.common.exceptions import WebDriverException
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
#
#
# def _create_chrome(options: Options):
#     try:
#         return webdriver.Chrome(options=options)
#     except WebDriverException:
#         service = Service(ChromeDriverManager().install())
#         return webdriver.Chrome(service=service, options=options)
#
#
# @pytest.fixture
# def driver():
#     options = Options()
#     options.add_argument("--start-maximized")
#     options.add_argument("--disable-blink-features=AutomationControlled")
#     options.add_experimental_option("excludeSwitches", ["enable-automation"])
#     options.page_load_strategy = "eager"
#
#     browser = _create_chrome(options)
#     browser.implicitly_wait(5)
#
#     yield browser
#
#     browser.quit()


@pytest.fixture(scope="function")
def init_setup():
    print("\n 初始化环境")
    yield
    print(" 清理测试环境")

@pytest.fixture()
def generate_two_random_numbers():
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)
    return number_1, number_2

@pytest.fixture()
def expect_add(generate_two_random_numbers:tuple[int,int] ):
    number_1, number_2 = generate_two_random_numbers
    return number_1+number_2

@pytest.fixture()
def expect_sub(generate_two_random_numbers:tuple[int,int]):
    number_1, number_2 = generate_two_random_numbers
    return number_1-number_2

@pytest.fixture()
def expect_mul(generate_two_random_numbers:tuple[int,int]):
    number_1, number_2 = generate_two_random_numbers
    return number_1*number_2

@pytest.fixture()
def expect_div(generate_two_random_numbers:tuple[int,int]):
    number_1, number_2 = generate_two_random_numbers
    return number_1/number_2