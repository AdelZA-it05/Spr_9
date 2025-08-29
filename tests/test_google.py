import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# options = webdriver.ChromeOptions()
# driver = webdriver.Chrome(options=options)


options = webdriver.ChromeOptions()
options.add_argument("--headless")  # можно убрать если хочешь видеть браузер (через VNC)
driver = webdriver.Remote(
command_executor="http://selenium:4444/wd/hub",
options=options
)

def test_google_title(driver):
    driver.get("https://www.google.com")
    assert "Google" in driver.title
    driver.quit()
