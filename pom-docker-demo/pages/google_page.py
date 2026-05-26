from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class GooglePage(BasePage):
    SEARCH_BOX = (By.NAME, "q")

    def search(self, text):
        self.find(self.SEARCH_BOX).send_keys(text + "\n")
