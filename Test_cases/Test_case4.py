from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://fitpeo.com/revenue-calculator")

#slider element location
slider_min = driver.find_element(By.XPATH,"//span[@class='MuiSlider-thumb MuiSlider-thumbSizeMedium MuiSlider-thumbColorPrimary MuiSlider-thumb MuiSlider-thumbSizeMedium MuiSlider-thumbColorPrimary css-1sfugkh']")
#slider_max = driver.find_element(By.XPATH,"//span[@class='MuiSlider-thumb MuiSlider-thumbSizeMedium MuiSlider-thumbColorPrimary MuiSlider-thumb MuiSlider-thumbSizeMedium MuiSlider-thumbColorPrimary css-1sfugkh']")

print("before moving")
print(slider_min.location)

time.sleep(5)
act = ActionChains(driver)
act.drag_and_drop_by_offset(slider_min,57,0).perform()

print("location of slider after moving")
print(slider_min.location)

#text box location
text_box = driver.find_element(By.XPATH,"//input[@id=':R57alklff9da:']")
print(text_box.text)

slider = driver.find_element(By.XPATH,"//h5[normalize-space()='Total Gross Revenue Per Year']")
driver.execute_script("arguments[0].scrollIntoView();",slider)
time.sleep(5)

# # Calculate for slider value to 820
# min_value = int(slider.get_attribute("min"))
# max_value = int(slider.get_attribute("max"))
# current_value = int(slider.get_attribute("value"))
# desired_value = 820

# Calculate the required offset
# slider_width = slider.size['width']
# offset = (desired_value - current_value) / (max_value - min_value) * slider_width
#
# # Move the slider
# actions = ActionChains(driver)
# actions.click_and_hold(slider).move_by_offset(offset, 0).release().perform()