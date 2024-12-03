import time

from selenium import webdriver
from selenium.webdriver.common.by import By

ops = webdriver.ChromeOptions()
ops.add_argument("disable-notifications")
 
driver = webdriver.Chrome(options=ops)
driver.maximize_window()


driver.get("https://www.gps-coordinates.net/my-location")
time.sleep(5)
