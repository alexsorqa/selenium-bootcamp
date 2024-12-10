from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

SEARCH_BUTTON = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
CART_ICON = (By.CSS_SELECTOR, "div[data-test='@web/CartIcon']")


@given('Open Target page')
def open_target(context):
    context.driver.get('https://www.target.com/')


@when('Search for {product}')
def search_product(context, product):
    context.driver.find_element(By.ID, 'search').send_keys(product)
    context.driver.wait.until(EC.element_to_be_clickable(SEARCH_BUTTON)).click()


@then('Click on cart icon')
def click_cart_icon(context):
    context.driver.find_element(*CART_ICON).click()