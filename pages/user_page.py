from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class UserPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def go_to_admin(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[text()='Admin']")
        )).click()

    def click_add(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[normalize-space()='Add']")
        )).click()

        # Esperar que cargue el formulario
        self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//h6[text()='Add User']")
        ))

    def create_user(self, username, password):

        # Scroll (importante)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Seleccionar User Role
        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "(//div[contains(@class,'oxd-select-text')])[1]")
        )).click()

        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[text()='Admin']")
        )).click()

        # Employee Name (el campo más problemático)
        emp = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//input[contains(@placeholder,'Type')]")
        ))
        emp.clear()
        emp.send_keys("Admin")

        time.sleep(2)  # dejar cargar sugerencias

        # Seleccionar primera opción
        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "(//div[@role='option'])[1]")
        )).click()

        time.sleep(2)

        # Username
        inputs = self.driver.find_elements(By.XPATH, "//input[contains(@class,'oxd-input')]")
        inputs[1].send_keys(username)

        # Status
        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "(//div[contains(@class,'oxd-select-text')])[2]")
        )).click()

        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[text()='Enabled']")
        )).click()

        # Passwords
        password_inputs = self.driver.find_elements(By.XPATH, "//input[@type='password']")
        password_inputs[0].send_keys(password)
        password_inputs[1].send_keys(password)

        # Guardar
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

        time.sleep(3)