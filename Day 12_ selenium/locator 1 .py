from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# option = webdriver.ChromeOptions()
# driver = webdriver.Chrome(options=option)
driver.maximize_window()
driver.get("https://demo.nopcommerce.com/")
#driver.find_element(By.ID,"small-searchterms").send_keys("laptop")
driver.find_element(By.NAME,"q").send_keys("laptop")
# driver.find_element(By.LINK_TEXT,"Register").click()
driver.find_element(By.PARTIAL_LINK_TEXT,"Reg").click()