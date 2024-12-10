from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


COLORS = (By.XPATH, "//div[@data-test='@web/VariationComponent']//ul/li")


@then('{product} colors are visible')
def product_colors_visible(context, product):
    colors = context.driver.find_elements(*COLORS)
    total_colors = list(map(lambda x: x.text.strip().split('\n'), colors))
    total_colors = [el for elem in total_colors for el in elem]

    main_color = sorted(['Starlight Blue', 'Galactic Purple', 'Midnight Black'])
    total = sorted(list(filter(lambda x: x in main_color, total_colors)))
    assert main_color == total, f"Expected {main_color} but got {total}"