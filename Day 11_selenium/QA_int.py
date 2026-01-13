import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.implicitly_wait(5)

driver.get("https://www.yatra.com/")
driver.find_element(By.XPATH,"//section[@class='style_box__dORVf']/span/img[@alt='cross']").click()
time.sleep(10)
driver.find_element(By.XPATH,"//p[@title='New Delhi']").click()
driver.find_element(By.XPATH,"//input[@id='input-with-icon-adornment']").send_keys("BOM")
time.sleep(50 )