import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.britannica.com/topic/list-of-countries-1993160")

#1.scroll down page by pixel
# driver.execute_script("window.scrollBy(0,2000)","") # Java script syntax as per user 2000 pixel selected
# time.sleep(5)
# value = driver.execute_script("return window.pageYOffset;")
# print("pixel moved",value)

#2.Scroll down the page till element visible
# flag = driver.find_element(By.XPATH,"//a[normalize-space()='India']")
# driver.execute_script("arguments[0].scrollIntoView();",flag) # by giving xpath of a webelement
# value = driver.execute_script("return window.pageYOffset;")
# print("pixel moved",value)

#3.scroll down till end
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(5)
value = driver.execute_script("return window.pageYOffset;")
print("pixel moved",value)

time.sleep(5)
#4. scroll upto top position
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
value = driver.execute_script("return window.pageYOffset;")
print("pixel moved",value)