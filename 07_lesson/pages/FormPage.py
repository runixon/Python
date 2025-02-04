from selenium.webdriver.common.by import By

class FormPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"

    def open(self):
        self.driver.get(self.url)

    def fill_field(self, field_name, value):
        self.driver.find_element(By.NAME, field_name).send_keys(value)

    def submit_form(self):
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    def is_field_highlighted_green(self, field_id):
        field = self.driver.find_element(By.ID, field_id)
        return "alert-success" in field.get_attribute("class")

    def is_field_highlighted_red(self, field_id):
        field = self.driver.find_element(By.ID, field_id)
        return "alert-danger" in field.get_attribute("class")