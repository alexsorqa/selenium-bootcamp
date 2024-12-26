from pages.base_page import BasePage
from pages.cart_page import CartPage
from pages.header import Header
from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage
from pages.sign_in_menu import SignInMenu
from pages.sign_in_page import SignInPage
from pages.add_product_menu import AddProductMenu
from pages.terms_and_conditions_page import TermsAndConditions
from pages.returns_page import ReturnsPage


class Application:

    def __init__(self, driver):
        self.driver = driver

        self.base_page = BasePage(driver)
        self.header = Header(driver)
        self.main_page = MainPage(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.cart_page = CartPage(driver)
        self.sign_in_menu = SignInMenu(driver)
        self.sign_in_page = SignInPage(driver)
        self.add_product_menu = AddProductMenu(driver)
        self.terms_and_conditions_page = TermsAndConditions(driver)
        self.returns_page = ReturnsPage(driver)