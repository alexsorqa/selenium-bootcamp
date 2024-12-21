from behave import given, when, then


@then('Click header sign in')
def click_header_sign_in(context):
    context.app.header.click_sign_in_header()


@when('Search for {product}')
def search_product(context, product):
    context.app.header.search_product(product)


@then('Click on cart icon')
def click_cart_icon(context):
    context.app.header.click_cart_icon()