import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://jqueryui.com/slider/#range")
time.sleep(5)
min_slider = driver.find_element(By.XPATH,"//span[1]")
max_slider = driver.find_element(By.XPATH,"//span[2]")

print("before moving")
print(min_slider.location)
print(max_slider.location)
#time.sleep(5)
act = ActionChains(driver)
act.drag_and_drop_by_offset(min_slider,20,0).perform()
act.drag_and_drop_by_offset(max_slider,-30,0).perform()

print("location of slider after moving")
print(min_slider.location)
print(max_slider.location)