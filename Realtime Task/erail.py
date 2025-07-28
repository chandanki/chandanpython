from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://erail.in/")
driver.find_element(By.XPATH,"//input[@id='txtStationFrom']").clear()
driver.find_element(By.XPATH,"//input[@id='txtStationFrom']").send_keys("DEL")
time.sleep(5)
out = driver.find_element(By.XPATH,"//div[starts-with(@id,'Autocomplete_1740')]/div").text
print(out)