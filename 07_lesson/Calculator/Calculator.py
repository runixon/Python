from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Calc:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)  # Увеличиваем таймаут до 50 секунд

    def open(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def set_delay(self, delay):
        delay_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys(delay)

    def click_button(self, button_text):
        self.driver.find_element(By.XPATH, f"//span[text()='{button_text}']").click()

    def get_result(self):
        # Ждем, пока на экране появится результат (не пустая строка)
        self.wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))
        return self.driver.find_element(By.CSS_SELECTOR, ".screen").text
