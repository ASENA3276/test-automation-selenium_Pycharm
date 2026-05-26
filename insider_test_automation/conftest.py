import pytest
from utils.driver_factory import get_driver

@pytest.fixture
def driver():
    driver = get_driver()  # Driver oluştur
    yield driver  # Teste ver
    driver.quit()  # Test bitince kapat