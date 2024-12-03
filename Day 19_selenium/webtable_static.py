import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(5)

# count no. of rows and columns
noofrows = len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr"))
noofcols = len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr[1]/th"))

print("No.of rows",noofrows)
print("No. of col",noofcols)

# driver.get("https://demo.guru99.com/test/web-table-element.php")
#
#count no. of rows and columns
# noofrows = len(driver.find_elements(By.XPATH,"//table[@class='dataTable']//tr"))
# noofcols = len(driver.find_elements(By.XPATH,"//table[@class='dataTable']//tr[1]/th"))
#
# print(len(noofrows))
# print(len(noofcols))

#Read specific rows and columns
# spec = driver.find_element(By.XPATH,"//table[@name='BookTable']//tr[5]/td[1]").text
# print(spec)

#read all the rows and columns
print("all rows and columns")

# for r in range(2,noofrows+1):
#     for c in range(1,noofcols+1):
#         spec = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr["+str(r)+"]/td["+str(c)+"]").text
#         print(spec,end='     ')
#     print()

allrows = driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr/td")
# initialise sum variable
price_sum = 0

# for row in allrows:
#     price = driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr/td[4]")
#     column_value = price[1].text
#     if column_value.isdigit():
#         price_sum += int(column_value)
#     else:
#         price_sum += float(column_value)
#
# print(price_sum)

for r in range(2,noofrows+1):
    price = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr["+str(r)+"]/td[4]")
    value = int(price.text.strip())
    price_sum += value
    
print(price_sum)

