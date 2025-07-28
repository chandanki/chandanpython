from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

#driver = None


@pytest.fixture(scope='module') # scope = module is optional
def init_driver():
    global driver
    print("---------setup--------------")
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.google.com/")

 
    yield
    print("---tear down---")
    driver.quit()


@pytest.mark.usefixtures("init_driver")
def test_google():
    assert driver.title == "Google"
