from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class SearchResultsPage(BasePage):
    RESULT = (By.XPATH, "//div[@data-test = 'resultsHeading']/span")

    def generate_locator(self, product):
        return By.XPATH, f"//button[contains(@aria-label, 'Add {product}')]"

    def verify_search_results(self, product):
        result = self.driver.wait.until(EC.visibility_of_element_located(self.RESULT)).text
        result = result.strip().replace('“', "'").replace('”', "'")
        expected_result = f"for '{product}'"
        assert result == expected_result, f"Expected: {result}"

    def click_on_product(self, product):
        element = self.driver.find_element(By.CSS_SELECTOR, f"picture[data-test='@web/ProductCard/ProductCardImage/primary'] img[alt='{product}']")
        self.driver.wait.until((EC.element_to_be_clickable(element))).click()

    def add_to_cart(self, product):
        add_to_cart_locator = self.generate_locator(product)
        self.driver.wait.until(EC.element_to_be_clickable(add_to_cart_locator)).click()