from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from selenium.webdriver.support.ui import Select
from time import sleep


class ReturnsPage(BasePage):
    HELP_DD = (By.CSS_SELECTOR, "[id*='ViewHelpTopics']")
    HEADER_TXT = (By.XPATH, "//h1[text()=' {SUBSTRING}']")

    def open_returns_page(self):
        self.open_url("https://help.target.com/help/SubCategoryArticle?childcat=Returns&parentcat=Returns+%26+Exchanges")

    def _get_header_locator(self, text):
        return [self.HEADER_TXT[0], self.HEADER_TXT[1].replace('{SUBSTRING}', text)]

    def select_promotions(self, dd_option_value):
        dropdown = self.find_element(*self.HELP_DD)
        select = Select(dropdown)
        select.select_by_value(dd_option_value)

    def verify_topic_opened(self, selected_header):
        locator = self._get_header_locator(selected_header)
        self.wait_for_element_visible(locator)