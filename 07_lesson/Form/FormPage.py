from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FormPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    def fill(self, field_name, value):
        self.wait.until(EC.presence_of_element_located((By.NAME, field_name)))
        self.driver.find_element(By.NAME, field_name).send_keys(value)

    def submit(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    def is_green(self, field_name):
        field = self.driver.find_element(By.ID, field_name)
        result = "alert-success" in field.get_attribute("class")
        print(f"Field {field_name} is green: {result}")
        return result

    def is_red(self, field_name):
        field = self.driver.find_element(By.ID, field_name)
        result = "alert-danger" in field.get_attribute("class")
        print(f"Field {field_name} is red: {result}")
        return result