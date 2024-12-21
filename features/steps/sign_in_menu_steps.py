from behave import given, when, then


@then('Click sign in menu')
def click_sign_in_menu(context):
    context.app.sign_in_menu.click_sign_in()