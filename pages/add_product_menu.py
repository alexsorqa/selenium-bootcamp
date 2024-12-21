from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from time import sleep


class AddProductMenu(BasePage):
    ADD_PRODUCT_MENU_ADD = (By.CSS_SELECTOR, "button[data-test='orderPickupButton']")
    VIEW_CART_AND_CHECKOUT = (By.CSS_SELECTOR, "div a[href='/cart']")

    def add_menu_click_add_product(self):
        self.wait_and_click(self.ADD_PRODUCT_MENU_ADD)

    def view_cart_checkout(self):
        self.wait_and_click(self.VIEW_CART_AND_CHECKOUT)