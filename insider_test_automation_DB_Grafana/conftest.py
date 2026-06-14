import pytest
from utils.driver_factory import get_driver

@pytest.fixture
def driver():
    driver = get_driver()  # Driver oluştur
    yield driver  # Teste ver
    driver.quit()  # Test bitince kapat

    import pytest
    from datetime import datetime

    @pytest.hookimpl(hookwrapper=True)
    def pytest_runtest_makereport(item):
        outcome = yield
        rep = outcome.get_result()

        if rep.when == "call" and rep.failed:
            driver = item.funcargs.get("driver")
            if driver:
                file_name = f"screenshots/test_failure_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
                driver.save_screenshot(file_name)