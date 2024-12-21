from behave import given, when, then


@then('Verify sign in page open')
def verify_sign_in_page(context):
    context.app.sign_in_page.verify_sign_in_page()


@then('Input {username} username on sign in page')
def input_username_sign_in_page(context, username):
    context.app.sign_in_page.input_text_email_sign_in(username)


@then('Input {password} password on sign in page')
def input_password_sign_in_page(context, password):
    context.app.sign_in_page.input_password_sign_in(password)


@then('Click sign in on sign in page')
def click_sign_in_sign_in_page(context):
    context.app.sign_in_page.click_login_button_sign_in_page()
