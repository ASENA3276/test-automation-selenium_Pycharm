from selenium.webdriver.support.ui import WebDriverWait  # Explicit wait
from selenium.webdriver.support import expected_conditions as EC  # Expected conditions

def wait_for_element(driver, locator, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located(locator)  # Element görünene kadar bekler
    )

def wait_for_clickable(driver, locator, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(locator)  # Tıklanabilir olana kadar bekler
    )