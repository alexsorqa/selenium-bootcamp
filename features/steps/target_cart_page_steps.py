from selenium.webdriver.common.by import By
from behave import given, when, then


@then('Verify {item} on cart page')
def verify_item_cart_page(context, item):
    context.app.cart_page.verify_item_in_cart(item)
