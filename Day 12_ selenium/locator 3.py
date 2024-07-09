from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

#example of css selector using Tag and Id
# syntax tagname#value of Id eg. Input#username ,we can take #Id value too
driver.get("https://www.facebook.com/")
# driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("abc")

#by tagname and class
# syntax tagname.value of class
# driver.find_element(By.CSS_SELECTOR,".inputtext").send_keys("gmail.com")

#by tagname and attribute
#syntax tagname[attribute=value]
#driver.find_element(By.CSS_SELECTOR,"input[placeholder='Email address or phone number']").send_keys("FirstName")
#driver.find_element(By.CSS_SELECTOR,"input[data-testid= royal_email]").send_keys("no email found")

#by tagname,Class and attribute
driver.find_element(By.CSS_SELECTOR,"input.inputtext[data-testid= royal_pass]").send_keys("123jj")
