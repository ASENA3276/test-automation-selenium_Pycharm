from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.wait_utils import wait_for_element, wait_for_clickable

class JobsPage(BasePage):

    # Dropdownlar
    LOCATION_DROPDOWN = (By.XPATH, "//div[contains(text(),'Location')]")  # Location dropdown
    TEAM_DROPDOWN = (By.XPATH, "//div[contains(text(),'Team')]")          # Team dropdown

    # Job listesi ve Apply
    JOB_LIST = (By.XPATH, "//div[@class='posting']")                     # Job listesi
    APPLY_BUTTON = (By.XPATH, "//a[contains(text(),'Apply')]")           # Apply buton

    def filter_jobs(self):
        """
        Location ve Team dropdownlarından seçim yapar
        Explicit wait + clickable kullanılır
        """
        # ---------- Location ----------
        self.click(self.LOCATION_DROPDOWN)  # Dropdown aç

        # Istanbul seçeneğini dropdown açıldıktan sonra bekle ve click
        ISTANBUL_OPTION_DYNAMIC = (By.XPATH, "//div[contains(@class,'filter')]//a[contains(text(),'Istanbul')]")
        wait_for_clickable(self.driver, ISTANBUL_OPTION_DYNAMIC).click()

        # ---------- Team ----------
        self.click(self.TEAM_DROPDOWN)  # Dropdown aç

        # QA seçeneğini bekle ve click
        QA_OPTION_DYNAMIC = (By.XPATH, "//div[contains(@class,'filter')]//a[contains(text(),'Quality Assurance')]")
        wait_for_clickable(self.driver, QA_OPTION_DYNAMIC).click()

    def verify_jobs(self):
        """
        Job listesinde doğru pozisyon ve lokasyon kontrolü
        """
        jobs = wait_for_element(self.driver, self.JOB_LIST)  # Job listesini bekle
        all_jobs = self.driver.find_elements(*self.JOB_LIST)
        assert len(all_jobs) > 0, "Job list boş!"

        for job in all_jobs:
            text = job.text
            assert "Quality Assurance" in text, f"Expected 'Quality Assurance' in {text}"
            assert "Istanbul" in text, f"Expected 'Istanbul' in {text}"

    def click_apply(self):
        """
        Listedeki Apply butonuna tıkla
        """
        apply_btn = wait_for_clickable(self.driver, self.APPLY_BUTTON)  # Clickable bekle
        apply_btn.click()