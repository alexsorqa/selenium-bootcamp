from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Target page')
def open_target(context):
    context.driver.get('https://www.target.com/')
    sleep(3)


@when('Click Signin button')
def click_signin(context):
    context.driver.find_element(By.ID, "account-sign-in").click()
    sleep(3)
    context.driver.find_element(By.XPATH, "//button[@type='button' and contains(text(), 'Sign in')]").click()


@then('Verify Signin page open')
def verify_sign_in_page(context):
    context.driver.find_element(By.XPATH, "//span[contains(text(), 'Sign into your Target account')]")
