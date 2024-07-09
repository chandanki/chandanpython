from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
# driver.get("http://www.automationpractice.pl/index.php")
#driver.close()
# slider = driver.find_elements(By.CLASS_NAME,"homeslider-container")
# print(len(slider))
links = driver.find_elements(By.TAG_NAME,"a")
print(len(links))

driver.get("https://demo.guru99.com/test/web-table-element.php")
slider = driver.find_elements(By.TAG_NAME,"td")
print(len(slider))