import pytest
from pages.home_page import HomePage
from pages.careers_page import CareersPage
from pages.jobs_page import JobsPage
from pages.lever_page import LeverPage
from utils.screenshot_utils import take_screenshot

def test_insider_flow(driver):
    try:
        home = HomePage(driver)  # Home page objesi
        careers = CareersPage(driver)  # Careers page objesi
        jobs = JobsPage(driver)  # Jobs page objesi
        lever = LeverPage(driver)  # Lever page objesi

        home.go_to_homepage()  # Site aç
        assert "insiderone" in driver.current_url  # Ana sayfa doğrulama

        home.accept_cookies()  # Cookie kabul
        home.click_hiring()  # Hiring click

        careers.verify_careers_page()  # Careers doğrula
        careers.click_explore_roles()  # Explore roles
        careers.click_open_positions()  # Open positions

       # jobs.filter_jobs()  # Filtre uygula
        #jobs.verify_jobs()  # Liste doğrula

       # jobs.click_apply()  # Apply click

        #lever.verify_lever_page()  # Lever doğrula

    except Exception as e:
        take_screenshot(driver)  # Hata screenshot
        raise e  # Hata fırlat