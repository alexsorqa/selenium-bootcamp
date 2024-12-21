from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep


class TermsAndConditions(BasePage):

    def verify_terms_and_conditions(self):
        self.verify_partial_url('terms-conditions')