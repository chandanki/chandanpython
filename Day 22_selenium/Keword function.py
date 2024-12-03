from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains,Keys

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://text-compare.com/")
input1 = driver.find_element(By.XPATH,"//textarea[@id='inputText1']")
input2 = driver.find_element(By.XPATH,"//textarea[@id='inputText2']")

input1.send_keys("this is my second code")

act = ActionChains(driver)

# act = ActionChains(driver)  # 1st way
# act.key_down(Keys.CONTROL)
# act.send_keys("a")
# act.key_up(Keys.CONTROL)
# act.perform()

act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()   # 2nd way
act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

# act.send_keys(Keys.TAB)
# act.perform()

act.send_keys(Keys.TAB).perform()
act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

input1 = driver.find_element(By.XPATH,"//div[@class='compareButtonText']").click()

input1 = driver.find_element(By.XPATH,"//span[@class='messageForUser']").click()


