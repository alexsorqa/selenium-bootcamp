from selenium.webdriver.common.by import By
from behave import given, when, then


@then("Add to cart {item} in add product menu")
def add_to_cart_item_in_product_menu(context, item):
    context.app.add_product_menu.add_menu_click_add_product()


@then("Click view cart and checkout in product menu")
def view_and_click_checkout_product_menu(context):
    context.app.add_product_menu.view_cart_checkout()
