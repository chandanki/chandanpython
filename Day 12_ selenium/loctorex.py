from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.pristyncare.com/")
driver.find_element(By.XPATH,"//*[@class='popup-close-btn']").click()
driver.find_element(By.XPATH,"(//button[@name='sendOtpFormdata'])[1]https://www.pristyncare.com/gp/brand/?utm_source=google&utm_medium=cpc&campaign_id=19364633273&adgroup_id=143348269143&Keyword_Id=kwd-652393837669&Network=g&Device=c&Matchtype=e&Location=1007765&Keyword=pristyn%20care&Placement=&Ad_Position=&gcl_Id=CjwKCAjwp4m0BhBAEiwAsdc4aNkQbUUeluLhJMUZ4UGMhm0CoSPEho9SUpU-ZQMypkzgCzfA8N4CghoC5-sQAvD_BwE&awsearchcpc=1&gad_source=1&gclid=CjwKCAjwp4m0BhBAEiwAsdc4aNkQbUUeluLhJMUZ4UGMhm0CoSPEho9SUpU-ZQMypkzgCzfA8N4CghoC5-sQAvD_BwE]").click()