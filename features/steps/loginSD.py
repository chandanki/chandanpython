import time

from behave import *
from selenium  import webdriver
from selenium.webdriver.common.by import By


@given('launch chrome browser')
def launchbrowser(context):
    context.driver = webdriver.Chrome()

@when('open the orange HRM page')
def openloginpage(context):
    context.driver.get("https://www.orangehrm.com/")
    time.sleep(4)

@then('verify logo')
def verifylogo(context):
    status = context.driver.find_element(By.XPATH,"//a[@class='navbar-brand nav-logo']").is_displayed()
    assert status is True

@then('close Browser')
def closebrowser(context):
    context.driver.close()

