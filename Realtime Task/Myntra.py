import time

import document
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.myntra.com/?utm_source=dms_google")
driver.implicitly_wait(10)

profile = driver.find_element(By.XPATH,"//span[normalize-space()='Profile']").click()
driver.find_element(By.XPATH,"//a[@href='/contactus' and @data-track='coupons']").click()
