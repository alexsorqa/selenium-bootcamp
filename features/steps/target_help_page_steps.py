from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Target help page')
def open_target_help_page(context):
    context.driver.get('https://help.target.com/help')


@then('Verify UI elements present')
def verify_ui_elements_present(context):
    context.driver.find_element(By.XPATH, "//div/h2[contains(text(), 'Target Help')]")
    context.driver.find_element(By.CSS_SELECTOR, ".search-input")
    context.driver.find_element(By.CSS_SELECTOR, ".btn-sm.search-btn")

    elements = context.driver.find_elements(By.CSS_SELECTOR, "div.container.clearfix div.col-lg-12")[1].text
    total = list(map(lambda x: x, elements.split('\n')))
    print(total, len(total), sep='\n')

    elements_2 = context.driver.find_elements(By.CSS_SELECTOR, "div.container.clearfix div.col-lg-12")[2].text
    total_2 = list(map(lambda x: x.strip(), elements_2.strip().split('\n')))
    print(total_2, len(total_2), sep='\n')

    context.driver.find_element(By.CSS_SELECTOR, "div.home-container#divID1 h2")

