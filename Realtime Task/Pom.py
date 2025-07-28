from selenium import webdriver
from selenium.webdriver.common.by import By


class Login:
    text_box_username_id = "Email"
    text_box_id = "password"
    button_login = "//input[@id='login']"

    def __init__(self,driver):
        self.driver = driver

    def setUsername(self,username):
        self.driver.find_element(By.ID,self.text_box_username_id).send_keys("username")
    def SetPassword(self,password):
        self.driver.find_element(By.ID,self.text_box_id).send_keys("password")
    def Login(self):
        self.driver.find_element(By.XPATH,self.button_login).click()
# Now POM is done
# 2. is to create test cases named as test folder which is used as a pytest
