from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('Verify cart is empty')
def verify_cart_is_empty(context):
    context.driver.find_element(By.CSS_SELECTOR, "div[data-test='boxEmptyMsg'] h1")