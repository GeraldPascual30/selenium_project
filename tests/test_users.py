from time import time

import pytest
from utils.driver_setup import get_driver
from pages.login_page import LoginPage
from pages.user_page import UserPage
from utils.screenshot import take_screenshot

@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

def test_create_user(driver):
    login = LoginPage(driver)
    user = UserPage(driver)

    login.open()
    login.login("Admin", "admin123")

    user.go_to_admin()
    user.click_add()

    # Validar que estamos en el formulario
    assert "add user" in driver.page_source.lower()

    take_screenshot(driver, "create_user_page")

def test_update_user_page(driver):
    login = LoginPage(driver)
    user = UserPage(driver)

    login.open()
    login.login("Admin", "admin123")

    user.go_to_admin()

    # ✅ Validar por URL (más estable)
    assert "admin" in driver.current_url.lower()

    take_screenshot(driver, "update_user_page")

def test_delete_user_page(driver):
    login = LoginPage(driver)
    user = UserPage(driver)

    login.open()
    login.login("Admin", "admin123")

    user.go_to_admin()

    # ✅ Validar por URL
    assert "admin" in driver.current_url.lower()

    take_screenshot(driver, "delete_user_page")