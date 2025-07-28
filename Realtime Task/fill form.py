 import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://demoqa.com/automation-practice-form")
#driver.implicitly_wait(10)

#Filling form step by step
first_name = driver.find_element(By.XPATH,"//input[@id='firstName']").send_keys("champ")
last_name= driver.find_element(By.XPATH,"//input[@id='lastName']").send_keys("kumar")
email = driver.find_element(By.XPATH,"//input[@id='userEmail']").send_keys("user@gmail.com")
gender = driver.find_element(By.XPATH,"//label[normalize-space()='Male']").click()
mobile = driver.find_element(By.XPATH,"//input[@id='userNumber']").send_keys(1111122222)
time.sleep(5)
DOB = driver.find_element(By.XPATH,"//input[@id='dateOfBirthInput']").click() # Click Datepicker


month = Select(driver.find_element(By.XPATH,"//select[@class='react-datepicker__month-select']"))
month.select_by_visible_text("December") #month

year = Select(driver.find_element(By.XPATH,"//select[@class='react-datepicker__year-select']"))
year.select_by_visible_text("1993")  # year

dates = driver.find_elements(By.XPATH,"//div[@role='listbox']/div/div")
for date in dates:
    if date.text=="16":
        date.click()
        break
pic = driver.find_element(By.XPATH,"//input[@id='uploadPicture']").send_keys("C:/Users/DELL/OneDrive/Documents/FW rule.txt")

current_add = driver.find_element(By.XPATH,"//textarea[@id='currentAddress']").send_keys("Colony No. 4 ")

# state = Select(driver.find_element(By.XPATH,"//div[@id='state']//div[@class=' css-tlfecz-indicatorContainer']//*[name()='svg']"))
# state.select_by_visible_text("Haryana")
submit = driver.find_element(By.XPATH,"//button[@class='btn btn-primary']")
driver.execute_script("arguments[0].scrollIntoView();", submit)
submit.click()
name = driver.find_element(By.XPATH,"//table[@class='table table-dark table-striped table-bordered table-hover']//tr[1]/td[2]").text
print(name)
time.sleep(5)

