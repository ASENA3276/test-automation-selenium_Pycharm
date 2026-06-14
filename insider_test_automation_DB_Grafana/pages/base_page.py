from utils.wait_utils import wait_for_element, wait_for_clickable  # Wait fonksiyonları
from utils.retry_utils import retry  # Retry mekanizması

class BasePage:

    def __init__(self, driver):
        self.driver = driver  # Driver referansı

    def click(self, locator):
        retry(lambda: wait_for_clickable(self.driver, locator).click())  # Retry + wait ile click

    def get_text(self, locator):
        return wait_for_element(self.driver, locator).text  # Text al

    def is_visible(self, locator):
        return wait_for_element(self.driver, locator).is_displayed()  # Görünürlük kontrolü

    def get_current_url(self):
        return self.driver.current_url  # URL al