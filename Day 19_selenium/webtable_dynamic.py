from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com/")

#no . of rows
noofrows = len(driver.find_elements(By.XPATH,"//table[@id='taskTable']//tr"))
print(noofrows)