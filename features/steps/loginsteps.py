import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('I launch Chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome()
@when('I open Orange HRM Homepage')
def step_impl(context):
    context.driver.get("https://practicetestautomation.com/practice-test-login/")

#time.sleep(50)
#webdriver.implicitly_wait(10)
@when('Enter username "{user}" and password "{pwd}"')
def step_impl(context,user,pwd):
    context.driver.find_element(By.XPATH,"//input[@id='username']").send_keys(user)
    context.driver.find_element(By.XPATH,"//input[@id='password']").send_keys(pwd)
@when('Click on login button')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//button[@id='submit']").click()
@then('User must login to the dashboard')
def step_impl(context):
    try:
        text = context.driver.find_element(By.XPATH,"//h1[normalize-space()='Logged In Successfully']").text
    except:
        context.driver.close()
        assert False,"Test Failed"
    if text == "Logged In Successfully":
        context.driver.close()
        assert True,"Test Passed"


