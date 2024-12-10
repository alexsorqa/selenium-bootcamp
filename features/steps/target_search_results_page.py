from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

RESULT = (By.XPATH, "//div[@data-test = 'resultsHeading']/span")
ORDER_PICKUP_BUTTON = (By.CSS_SELECTOR, "button[data-test='orderPickupButton']")
CART = (By.XPATH, "//div/a[@href='/cart']")


def generate_add_to_cart_locator(product):
    return By.XPATH, f"//button[contains(@aria-label, 'Add {product}')]"


@then('{product} result is displayed')
def display_result(context, product):
    result = context.driver.wait.until(EC.visibility_of_element_located(RESULT)).text
    result = result.strip().replace('“', "'").replace('”', "'")
    expected_result = f"for '{product}'"
    assert result == expected_result, f"Expected: {result}"


@then('Click on {product} in results page')
def click_on_product(context, product):
    element = context.driver.find_element(By.CSS_SELECTOR, f"picture[data-test='@web/ProductCard/ProductCardImage/primary'] img[alt='{product}']")
    context.driver.wait.until((EC.element_to_be_clickable(element))).click()


@then('Add to cart {product} in results page')
def add_to_cart_product(context, product):
    add_to_cart_locator = generate_add_to_cart_locator(product)
    context.driver.wait.until(EC.element_to_be_clickable(add_to_cart_locator)).click()
    """context.driver.wait.until(EC.element_to_be_clickable(ORDER_PICKUP_BUTTON)).click()
    context.driver.wait.until(EC.element_to_be_clickable(CART)).click()"""




