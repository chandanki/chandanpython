from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://jqueryui.com/datepicker/")
driver.switch_to.frame(0)
#driver.find_element(By.XPATH,"//input[@id='datepicker']").send_keys("11/01/2024")

# Send the date to the datepicker input field
date_input = driver.find_element(By.XPATH, "//input[@id='datepicker']")
date_input.send_keys("11/01/2024")

# Retrieve and print the date from the input field
entered_date = date_input.get_attribute("value")
print("Entered Date:", entered_date)

driver.quit()