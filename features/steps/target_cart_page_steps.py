from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('Verify {item} on cart page')
def verify_item_cart_page(context, item):
    context.driver.find_element(By.XPATH, "//div/div[contains(text(), 'Blogilates Gym Bag - Black')]")