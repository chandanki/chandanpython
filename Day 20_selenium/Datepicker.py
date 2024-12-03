from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://jqueryui.com/datepicker/")
driver.switch_to.frame(0)
driver.find_element(By.XPATH,"//input[@id='datepicker']").send_keys("11/01/2024")