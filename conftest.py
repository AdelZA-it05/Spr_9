import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service

# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service)


# @pytest.fixture
# def driver():
#     options = webdriver.ChromeOptions()
#     driver = webdriver.Chrome(options=options)
#     yield driver
#     driver.quit()


# @pytest.fixture
# def driver():
#     options = webdriver.ChromeOptions()
#     options.add_argument("--headless")  # можно убрать если хочешь видеть браузер (через VNC)
#     driver = webdriver.Remote(
#         command_executor="http://selenium:4444/wd/hub",
#         options=options
#     )
#     yield driver
#     driver.quit()


# @pytest.fixture
# def driver():
#     options = get_default_chrome_options()
#     driver = webdriver.Remote(command_executor="http://127.0.0.1:4444/wd/hub", options=options)
#     driver = webdriver.Remote(
#         command_executor="http://127.0.0.1:4444/wd/hub",
#         desired_capabilities={
#             "browserName": "chrome",
#             "version": "latest"
#         }
#     )
#     yield driver
#     driver.quit()

# def get_default_chrome_options():
#     options = webdriver.ChromeOptions()
#     options.add_argument("--no-sandbox")
#     return options