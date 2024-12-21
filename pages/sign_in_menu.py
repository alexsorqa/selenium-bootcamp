from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep


class SignInMenu(BasePage):
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, "button[data-test='accountNav-signIn']")

    def click_sign_in(self):
        self.wait_and_click(self.SIGN_IN_BUTTON)