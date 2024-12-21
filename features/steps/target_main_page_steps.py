from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open Target page')
def open_target(context):
    context.app.main_page.open_main()


@then('Target main page opens')
def verify_target_main_page(context):
    context.app.header.verify_target_cart_icon()
