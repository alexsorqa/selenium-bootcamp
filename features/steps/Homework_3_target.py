from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('Click on cart icon')
def click_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, "div[data-test='@web/CartIcon']").click()
    sleep(3)


@then('Verify cart is empty')
def verify_cart_is_empty(context):
    context.driver.find_element(By.CSS_SELECTOR, "div[data-test='boxEmptyMsg'] h1")