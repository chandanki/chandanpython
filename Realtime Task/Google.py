import time

from behave import *
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.google.co.in/")
driver.implicitly_wait(10)

driver.find_element(By.XPATH,"//textarea[contains(@data-ved, '0ahUK')]").send_keys("value")
search = driver.find_element(By.XPATH,"//textarea[contains(@data-ved, '0ahUK')]").get_attribute("value")
print(search)

