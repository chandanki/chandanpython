
    import time

from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()

# driver.get("https://www.amazon.in/")

#
# # handling of search suggestion and selecting 4 th item
# driver.find_element(By.XPATH,"//input[@id='twotabsearchtextbox']").send_keys("Redmi")
# driver.find_element(By.XPATH,"//div[@class='left-pane-results-container']/div[4]").click()

driver.get("https://force-us-staging-identity.moj.io/account/signinmojio?clientid=2cacee42-2dc1-456a-aebe-616bbcea07d0&returnurl=%2Fconnect%2Fauthorize%2Fcallback%3Fclient_id%3D2cacee42-2dc1-456a-aebe-616bbcea07d0%26redirect_uri%3Dhttps%3A%2F%2Fforce-us-staging.moj.io%2F%26response_type%3Dtoken%26scope%3Dfull")
driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//input[@id='input-email']").send_keys("forcenew21@moj.io")
driver.find_element(By.XPATH,"//input[@id='input-password']").send_keys("forcefleet")
driver.find_element(By.XPATH,"//input[@id='action-button']").click()

# driver.find_element(By.XPATH,"//span[normalize-space()='Drivers']").click()
# title = driver.find_element(By.XPATH,"//h2[normalize-space()='Dashboard']").text
# print(title)
#Explicit wait
# wait = WebDriverWait(driver, 20)
# element = wait.until(EC.visibility_of_element_located((By.XPATH,"//span[contains(normalize-space() ,'Vehicles')]")))
# element.click()
#attempt 1
# try:
#     dashboard_element = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.XPATH, "//span[contains(normalize-space() ,'Vehicles')]")))
#     WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.ID, "//span[contains(normalize-space() ,'Vehicles')]"))).click()
# except TimeoutException:
#     print("Time out ho gya")

#attempt 2
time.sleep(10)
dashboard_element = driver.find_element(By.XPATH, "//span[normalize-space()='Vehicles']")
driver.execute_script("arguments[0].scrollIntoView(true);", dashboard_element)
dashboard_element.click()
time.sleep(5)


# wait = WebDriverWait(driver, 10)
# element = wait.until(EC.element_to_be_clickable((By.XPATH,"//span[normalize-space()='Drivers']")))
# element.click()
# wait = WebDriverWait(driver, 10)
# element = wait.until(EC.element_to_be_clickable((By.XPATH,"//span[normalize-space()='Clips']")))
# element.click()
#driver.find_element(By.XPATH,"//span[normalize-space()='Drivers']").click()
time.sleep(5)
# driver.find_element(By.XPATH,"//span[contains(normalize-space() ,'Vehicles')]").click()
# time.sleep(5)
# title_one = driver.find_element(By.XPATH,"//h2[normalize-space()='Vehicles']").text
# print(title_one)


