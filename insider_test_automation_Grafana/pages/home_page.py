from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):

    COOKIE_ACCEPT = (By.ID, "wt-cli-accept-all-btn")  # Cookie buton
    WE_ARE_HIRING = (By.XPATH, "//a[text()=\"We're hiring\"]")  # Hiring link

    def go_to_homepage(self):
        self.driver.get("https://insiderone.com/")  # Ana sayfaya git

    def accept_cookies(self):
        self.click(self.COOKIE_ACCEPT)  # Cookie kabul et

    def click_hiring(self):
        self.click(self.WE_ARE_HIRING)  # Hiring linkine tıkla