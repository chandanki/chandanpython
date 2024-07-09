# from selenium import webdriver
#
# option = webdriver.ChromeOptions()
# driver = webdriver.Chrome(options=option)
# driver.maximize_window()
import time

#approach 2

from selenium import webdriver
from selenium.webdriver.common.by import By

# option = webdriver.ChromeOptions()
# driver = webdriver.Chrome(options=option)
driver = webdriver.Chrome()
driver.maximize_window()
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
#
# driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("chasy")
# driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("chasy001")
# driver.find_elements(By.XPATH, "//button[@type='submit']").click()
# driver.close()

driver.get("https://dev.shipease.in/login")


username = driver.find_element(By.XPATH, "//input[@autocomplete='new-username']")
username.send_keys("8090831663")

password = driver.find_element(By.CSS_SELECTOR, "input[type='password']")
password.send_keys("superuser")


login = driver.find_element(By.XPATH, "//button[@type='submit']")
login.click()