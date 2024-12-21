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


@given('Store original window')
def store_original_window(context):
    context.original_window = context.app.sign_in_page.get_current_window_handle()


@then('Click on terms and conditions link')
def click_terms_and_conditions_link(context):
    context.app.sign_in_page.click_terms_and_conditions()


@when('Switch to new window')
def switch_window(context):
    context.app.sign_in_page.switch_to_new_window()


@then('Switch back to original window')
def switch_to_original_window(context):
    context.app.terms_and_conditions_page.switch_to_window_by_id(context.original_window)
