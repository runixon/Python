import pytest
from selenium import webdriver
from Shop import ShopPage
import allure

# Константы для теста
USERNAME = "standard_user"
PASSWORD = "secret_sauce"

ITEMS_TO_ADD = [
    "Sauce Labs Backpack",
    "Sauce Labs Bolt T-Shirt",
    "Sauce Labs Onesie"
]

FIRST_NAME = "Иван"
LAST_NAME = "Петров"
ZIP_CODE = "103274"

EXPECTED_TOTAL = "$58.29"

@pytest.fixture(scope="function")
def browser():
    """
    Фикстура для инициализации и завершения работы браузера.
    """
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@allure.title("Тест покупки товаров в интернет-магазине")
@allure.description("Проверка корректности итоговой стоимости заказа")
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_shopping(browser):
    """
    Тест, который проверяет процесс покупки товаров в интернет-магазине.
    """
    test = ShopPage(browser)

    with allure.step("Открытие главной страницы магазина"):
        test.open()

    with allure.step(f"Вход в систему с логином {USERNAME} и паролем {PASSWORD}"):
        test.login(USERNAME, PASSWORD)

    with allure.step("Добавление товаров в корзину"):
        for item_name in ITEMS_TO_ADD:
            test.add_item(item_name)

    with allure.step("Переход в корзину"):
        test.cart()

    with allure.step("Переход к оформлению заказа"):
        test.checkout()

    with allure.step(f"Заполнение информации для заказа: {FIRST_NAME}, {LAST_NAME}, {ZIP_CODE}"):
        test.checkout_info(FIRST_NAME, LAST_NAME, ZIP_CODE)

    with allure.step("Проверка итоговой стоимости заказа"):
        total_price = test.total_price()
        assert total_price == f"Total: {EXPECTED_TOTAL}", (
            f"Итоговая стоимость не совпадает. Ожидалось: {EXPECTED_TOTAL}, "
            f"Фактически: {total_price}"
        )