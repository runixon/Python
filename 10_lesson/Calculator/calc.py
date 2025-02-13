import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Calc:
    """
    Класс для взаимодействия с калькулятором на веб-странице.
    """

    def __init__(self, driver):
        """
        Инициализация класса.
        :param driver: WebDriver - экземпляр веб-драйвера Selenium.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)  # Увеличиваем таймаут до 50 секунд

    @allure.step("Открытие страницы калькулятора")
    def open(self) -> None:
        """
        Открывает страницу с калькулятором.
        """
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    @allure.step("Установка задержки вычислений")
    def set_delay(self, delay: str) -> None:
        """
        Устанавливает задержку вычислений в калькуляторе.
        :param delay: str - значение задержки в секундах.
        """
        delay_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys(delay)

    @allure.step("Нажатие кнопки {button_text}")
    def click_button(self, button_text: str) -> None:
        """
        Нажимает кнопку на калькуляторе по тексту.
        :param button_text: str - текст кнопки, которую нужно нажать.
        """
        self.driver.find_element(By.XPATH, f"//span[text()='{button_text}']").click()

    @allure.step("Получение результата вычислений")
    def get_result(self) -> str:
        """
        Ожидает появления результата и получает его с экрана калькулятора.
        :return: str - строка с результатом вычислений.
        """
        self.wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))
        return self.driver.find_element(By.CSS_SELECTOR, ".screen").text