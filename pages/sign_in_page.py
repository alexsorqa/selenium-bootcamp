from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep


class SignInPage(BasePage):
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login")

    def verify_sign_in_page(self):
        self.verify_partial_url('create_session_signin')

    def input_text_email_sign_in(self, username):
        self.input_text(username, *self.USERNAME)

    def input_password_sign_in(self, password):
        self.input_text(password, *self.PASSWORD)

    def click_login_button_sign_in_page(self):
        self.click(*self.LOGIN_BUTTON)