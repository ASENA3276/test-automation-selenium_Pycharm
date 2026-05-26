from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CareersPage(BasePage):

    EXPLORE_ROLES = (By.XPATH, "//span[text()='Explore open roles']")  # Buton
    OPEN_POSITIONS = (By.XPATH, "//a[contains(text(),'Open Positions')]")  # xx Open Positions

    def verify_careers_page(self):
        assert "careers" in self.get_current_url()  # URL doğrulama

    def click_explore_roles(self):
        self.click(self.EXPLORE_ROLES)  # Explore buton

    def click_open_positions(self):
        self.click(self.OPEN_POSITIONS)  # Open positions