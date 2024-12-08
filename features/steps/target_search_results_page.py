from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('{product} result is displayed')
def display_result(context, product):
    result = context.driver.find_element(By.XPATH, "//div[@data-test = 'resultsHeading']/span").text
    result = result.strip().replace('“', "'").replace('”', "'")
    expected_result = f"for '{product}'"
    assert result == expected_result, f"Expected: {result}"


@then('Add to cart {product} in results page')
def add_to_cart_product(context, product):
    context.driver.find_element(By.XPATH, f"//button[@aria-label='Add {product} to cart']").click()
    sleep(2)
    price = context.driver.find_element(By.CSS_SELECTOR, "span[data-test='product-price']").text
    assert price == "$39.99", f"Expected: $39.99, but got {price}"
    context.driver.find_element(By.CSS_SELECTOR, "button[data-test='orderPickupButton']").click()
    sleep(2)
    context.driver.find_element(By.XPATH, "//div/a[@href='/cart']").click()




