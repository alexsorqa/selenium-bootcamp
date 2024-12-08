from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Target page')
def open_target(context):
    context.driver.get('https://www.target.com/')


@when('Search for {product}')
def search_product(context, product):
    context.driver.find_element(By.ID, 'search').send_keys(product)
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    sleep(5)


@then('Click on cart icon')
def click_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, "div[data-test='@web/CartIcon']").click()