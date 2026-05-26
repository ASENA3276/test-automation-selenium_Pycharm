import time
import os

def take_screenshot(driver, name="screenshot"):
    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    file_path = os.path.join("screenshots", f"{name}_{timestamp}.png")
    driver.save_screenshot(file_path)
    print(f"Screenshot saved to {file_path}")