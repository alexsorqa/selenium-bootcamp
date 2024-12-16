from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open Target page')
def open_target(context):
    context.app.main_page.open_main()


@when('Search for {product}')
def search_product(context, product):
    context.app.header.search_product(product)


@then('Click on cart icon')
def click_cart_icon(context):
    context.app.header.click_cart_icon()