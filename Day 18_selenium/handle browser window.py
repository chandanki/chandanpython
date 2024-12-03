import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://admin:admin@the-internet.herokuapp.com/digest_auth")
windowid = driver.current_window_handle
print(windowid) #4138A563CA7959B7E7E654164F7559D3

driver.find_element(By.LINK_TEXT,'Elemental Selenium').click()
windowids = driver.window_handles
print(windowids)

# Approach 1
# parentwindow = windowids[0]
# childwindow = windowids[1]
# # print(parentwindow,childwindow)
# # switch id by their value as an array
# time.sleep(5)
#
# driver.switch_to.window(childwindow)
# print(driver.title)
#
# driver.switch_to.window(parentwindow)
# print(driver.title)

#Approach 2 by for loop

# for winid in windowids:
#     driver.switch_to.window(winid)
#     print(driver.title)

#close parent window

for winid in windowids:
    driver.switch_to.window(winid)
    if driver.title == 'The Internet':
        driver.close()




