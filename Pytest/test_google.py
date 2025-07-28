from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


def test_google():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.amazon.in/")
    driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']").send_keys("Redmi")
    driver.close()

def test_facebook():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.facebook.com/")
    driver.close()
