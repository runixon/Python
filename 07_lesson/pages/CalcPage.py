from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalcPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    def open(self):
        self.driver.get(self.url)

    def set_delay(self, delay):
        delay_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys(delay)

    def click_button(self, button_text):
        self.driver.find_element(By.XPATH, f"//span[text()='{button_text}']").click()

    def get_result(self, timeout):
        # Ожидаем, пока на экране появится конкретный результат (например, "15")
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
        )
        return self.driver.find_element(By.CSS_SELECTOR, ".screen").text