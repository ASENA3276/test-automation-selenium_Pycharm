from pages.google_page import GooglePage
from utils.driver_factory import create_driver


def test_google_search():
    driver = create_driver()
    google = GooglePage(driver)

    google.open("https://www.google.com")
    google.search("Selenium Docker")

    driver.quit()
