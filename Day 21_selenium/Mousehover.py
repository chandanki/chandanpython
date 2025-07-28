import time
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# driver.switch_to.new_window() # switch to new tab
# driver.get("https://www.britannica.com/topic/list-of-countries-1993160")
time.sleep(5)
#login
driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")
driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("admin123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()

#Admin,Usermanagement,User
#driver.find_element(By.XPATH,"//a[@class='oxd-main-menu-item active']//span[1]").click()
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[@class='oxd-main-menu-item active']"))
).click()
#driver.find_element(By.XPATH,"//span[normalize-space()='User Management']").click()
time.sleep(5)
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='User Management']"))
).click()