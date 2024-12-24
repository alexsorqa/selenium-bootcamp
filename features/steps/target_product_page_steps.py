from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


COLORS = (By.XPATH, "//div[@data-test='@web/VariationComponent']//ul/li")
COLOR_OPTIONS = (By.CSS_SELECTOR, "div[aria-label='Carousel'] li img")
SELECTED_COLOR = (By.CSS_SELECTOR, "[data-test='@web/VariationComponent'] div")


@then('{product} colors are visible')
def product_colors_visible(context, product):
    colors = context.driver.find_elements(*COLORS)
    total_colors = list(map(lambda x: x.text.strip().split('\n'), colors))
    total_colors = [el for elem in total_colors for el in elem]

    main_color = sorted(['Starlight Blue', 'Galactic Purple', 'Midnight Black'])
    total = sorted(list(filter(lambda x: x in main_color, total_colors)))
    assert main_color == total, f"Expected {main_color} but got {total}"


@given('Open shoes page')
def open_shoes_page(context):
    context.driver.get('https://www.target.com/p/A-91511634')


@then('Select different colors')
def select_different_colors(context):
    item_colors = context.driver.find_elements(*COLOR_OPTIONS)
    for color in item_colors:
        color.click()
        selected_color = context.driver.find_elements(*SELECTED_COLOR)[2].text
        print('Current color:', selected_color)