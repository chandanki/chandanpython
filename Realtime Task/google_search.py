import time

from behave import *
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.google.co.in/")
driver.implicitly_wait(10)

# handling of search suggestion and selecting 4 th item
field = driver.find_element(By.XPATH,"//textarea[@id='APjFqb']")
search = field.send_keys("Redmi")
time.sleep(5)
driver.find_element(By.XPATH,"//div[@id='Zrbbw']//div[1]//span[1]").click()
#field.send_keys(Keys.ENTER) # To click Enter this send_keys with Enter used
#capture cookies from browaser
cookies = driver.get_cookies()
print(len(cookies))

# for c in cookies:
#     print(c)
driver.add_cookie({"name":"My cookie","value":"123"})
cookies = driver.get_cookies()
print(len(cookies))

# for c in cookies:
#     print(c)
driver.delete_cookie("My cookie")
cookies = driver.get_cookies()
print(len(cookies))

# for c in cookies:
#      print(c)

driver.delete_all_cookies()
cookies = driver.get_cookies()
print(len(cookies))



