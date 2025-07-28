from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://groww.in/stocks/user/explore")
windowid = driver.current_window_handle
print(windowid)
driver.find_element(By.XPATH,"//input[@id = 'login_email1']").send_keys("rockystar.kumar42@gmail.com")
driver.find_element(By.XPATH,"//button[@type = 'button']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//input[@id = 'login_password1']").send_keys("chasy@007")
driver.find_element(By.XPATH,"//button[@type = 'button']").click()

time.sleep(5)