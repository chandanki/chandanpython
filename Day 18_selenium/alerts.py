import time

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://admin:admin@the-internet.herokuapp.com/digest_auth")

#driver.find_element(By.XPATH, "//a[normalize-space()='Digest Authentication']").click()
time.sleep(5)
# # alert = driver.switch_to.alert
# # alert.accept()
#
# driver.switch_to.alert.accept()

driver.close()