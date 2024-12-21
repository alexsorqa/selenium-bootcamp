from behave import given, when, then


@then('Verify terms and conditions page open')
def verify_terms_and_conditions_page_open(context):
    context.app.terms_and_conditions_page.verify_terms_and_conditions()


@then('Close current window')
def close_current_window(context):
    context.app.terms_and_conditions_page.close()

