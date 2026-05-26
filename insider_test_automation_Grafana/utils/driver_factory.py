from selenium import webdriver  # Selenium driver import
from selenium.webdriver.chrome.service import Service  # Chrome service
from webdriver_manager.chrome import ChromeDriverManager  # Driver auto install

def get_driver():
    options = webdriver.ChromeOptions()  # Chrome ayarları
    options.add_argument("--start-maximized")  # Tarayıcı tam ekran başlar

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)  # Driver oluştur
    driver.implicitly_wait(5)  # Global implicit wait (backup)
    return driver  # Driver döndür