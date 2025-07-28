from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Start WebDriver
driver = webdriver.Chrome()

# Open the website
driver.get("https://books-pwakit.appspot.com/")

# Wait for the shadow host to be present
shadow_host = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, "book-app"))
)

# Get the Shadow Root
shadow_root = driver.execute_script("return arguments[0].shadowRoot", shadow_host)

# Find elements inside the Shadow DOM using JavaScript
element_1 = driver.execute_script("return arguments[0].querySelector('app-header')", shadow_root)
element_2 = driver.execute_script("return arguments[0].querySelector('app-toolbar.toolbar-bottom')", element_1)
element_3 = driver.execute_script("return arguments[0].querySelector('book-input-decorator')", element_2)
input_field = driver.execute_script("return arguments[0].querySelector('input#input')", element_3)

# Interact with the input field
input_field.send_keys("My Name")

# Close WebDriver
driver.quit()
