import pytest
from utils.driver_setup import get_driver
from pages.login_page import LoginPage
from utils.screenshot import take_screenshot

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

# ✅ Camino feliz
def test_login_success(driver):
    login = LoginPage(driver)
    login.open()
    login.login("Admin", "admin123")

    # Esperar a que cargue el dashboard
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h6[text()='Dashboard']"))
    )

    take_screenshot(driver, "login_success")
    assert "dashboard" in driver.page_source.lower()

# ❌ Prueba negativa
def test_login_invalid(driver):
    login = LoginPage(driver)
    login.open()
    login.login("Admin", "wrongpass")

    take_screenshot(driver, "login_invalid")
    assert "invalid" in driver.page_source.lower()

# ⚠️ Prueba de límite (campos vacíos)
def test_login_empty(driver):
    login = LoginPage(driver)
    login.open()
    login.login("", "")

    take_screenshot(driver, "login_empty")
    assert "required" in driver.page_source.lower()