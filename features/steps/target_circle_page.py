from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Target Circle page')
def open_target_circle(context):
    context.driver.get('https://www.target.com/circle')


@then('{cells} benefit cells are displayed')
def validate_benefit_cells(context, cells):
    benefit_cells = context.driver.find_elements(By.CSS_SELECTOR, ".cell-item-content")
    assert len(benefit_cells) == int(14), f"Expected {cells}, but actual result {len(benefit_cells)}"

