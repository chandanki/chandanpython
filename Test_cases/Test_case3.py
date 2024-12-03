from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://fitpeo.com/revenue-calculator")

#Scroll down the page till revenue calculator slider
slider = driver.find_element(By.XPATH,"//h5[normalize-space()='Total Gross Revenue Per Year']")
driver.execute_script("arguments[0].scrollIntoView();",slider)
time.sleep(5)
value = driver.execute_script("return window.pageYOffset;")
print("pixel moved",value)