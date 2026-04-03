import os
from datetime import datetime

def take_screenshot(driver, name):
    if not os.path.exists("reports/screenshots"):
        os.makedirs("reports/screenshots")

    file_name = f"reports/screenshots/{name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    driver.save_screenshot(file_name)