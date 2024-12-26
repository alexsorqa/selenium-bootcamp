from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open Target returns page')
def open_target_returns_page(context):
    context.app.returns_page.open_returns_page()


@when('Select returns topic {dd_option_value}')
def select_promotions(context, dd_option_value):
    context.app.returns_page.select_promotions(dd_option_value)


@then('Verify returns {selected_header} page opened')
def verify_topic_opened(context, selected_header):
    context.app.returns_page.verify_topic_opened(selected_header)