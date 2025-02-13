import pytest
from selenium import webdriver
from calc import Calc
import allure


@pytest.fixture(scope="function")
def browser():
    """
    Фикстура для инициализации и завершения работы веб-драйвера.
    :return: WebDriver - экземпляр веб-драйвера.
    """
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@allure.title("Тест медленного калькулятора")
@allure.description("Проверяет корректность вычисления 7 + 8 = 15 с задержкой 45 секунд.")
@allure.feature("Функциональность калькулятора")
@allure.severity(allure.severity_level.CRITICAL)
def test_slow_calculator(browser):
    """
    Тест для проверки работы медленного калькулятора.
    :param browser: WebDriver - экземпляр веб-драйвера.
    """
    test = Calc(browser)

    with allure.step("Открытие страницы калькулятора"):
        test.open()

    with allure.step("Установка задержки в 45 секунд"):
        test.set_delay("45")

    with allure.step("Ввод выражения 7 + 8 ="):
        test.click_button("7")
        test.click_button("+")
        test.click_button("8")
        test.click_button("=")

    with allure.step("Получение результата и проверка корректности"):
        result = test.get_result()
        assert result == "15", "Результат на экране не равен 15"