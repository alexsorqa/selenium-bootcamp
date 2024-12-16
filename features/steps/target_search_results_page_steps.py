from selenium.webdriver.common.by import By
from behave import given, when, then


ORDER_PICKUP_BUTTON = (By.CSS_SELECTOR, "button[data-test='orderPickupButton']")
CART = (By.XPATH, "//div/a[@href='/cart']")


def generate_add_to_cart_locator(product):
    return By.XPATH, f"//button[contains(@aria-label, 'Add {product}')]"


@then('{product} result is displayed')
def display_result(context, product):
    context.app.search_results_page.verify_search_results(product)


@then('Click on {product} in results page')
def click_on_product(context, product):
    context.app.search_results_page.click_on_product(product)


@then('Add to cart {product} in results page')
def add_to_cart_product(context, product):
    context.app.search_results_page.add_to_cart(product)




