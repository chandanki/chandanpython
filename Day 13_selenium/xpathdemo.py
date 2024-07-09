from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("http://www.automationpractice.pl/index.php")
#full xpath
# driver.find_element(By.XPATH,"/html/body/div/div[1]/header/div[3]/div/div/div[2]/form/input[4]").send_keys("t shirts")
# driver.find_element(By.XPATH,"/html/body/div/div[1]/header/div[3]/div/div/div[2]/form/button").click()

#Relative xpath
# driver.find_element(By.XPATH,"//*[@id='search_query_top']").send_keys("t shirts")
# driver.find_element(By.XPATH,"//*[@id='searchbox']/button").click()

#or operator
# driver.find_element(By.XPATH,"//*[@id='search_query_top' or @name='search_query']").send_keys("t shirts")
# driver.find_element(By.XPATH,"//*[@id='searchbox']/button").click()

#and operator
# driver.find_element(By.XPATH,"//*[@id='search_query_top' and @name='search_query']").send_keys("t shirts")
# driver.find_element(By.XPATH,"//*[@id='searchbox']/button").click()

#contains and start with function for start and stop button
#syntax - //*[contains(@id,st)],,,,,//*[starts-with(@id,'st')]

driver.find_element(By.XPATH,"//input[contains(@id,'search')]").send_keys("t shirts")
driver.find_element(By.XPATH,"//button[starts-with(@name,'submit_')]").click()

#text function
driver.find_element(By.XPATH,"//a[text()='Women']").click()