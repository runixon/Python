import pytest
from selenium import webdriver
from FormPage import FormPage
import allure

@pytest.fixture(scope="function")
def driver():
    """
    Фикстура для инициализации и завершения работы браузера.
    """
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@allure.title("Тест отправки формы")
@allure.description("Проверка валидации полей формы после отправки")
@allure.feature("Форма")
@allure.severity(allure.severity_level.CRITICAL)
def test_form_submission(driver):
    """
    Тест, который проверяет валидацию полей формы после отправки.
    """
    test = FormPage(driver)

    with allure.step("Открытие страницы с формой"):
        test.open()

    form_data = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro"
    }

    with allure.step("Заполнение полей формы"):
        for field_name, value in form_data.items():
            test.fill(field_name, value)

    with allure.step("Отправка формы"):
        test.submit()

    with allure.step("Проверка, что поле 'zip-code' подсвечено красным"):
        assert test.is_red("zip-code"), "Поле 'zip-code' не подсвечено красным"

    with allure.step("Проверка, что остальные поля подсвечены зеленым"):
        for field_name in form_data.keys():
            assert test.is_green(field_name), f"Поле {field_name} не подсвечено зеленым"