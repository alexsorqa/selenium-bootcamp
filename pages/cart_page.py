from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class CartPage(BasePage):
    CART_EMPTY_TEXT = (By.CSS_SELECTOR, "div[data-test='boxEmptyMsg'] h1")

    def verify_cart_is_empty(self):
        self.find_element(*self.CART_EMPTY_TEXT)