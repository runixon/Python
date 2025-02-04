import pytest
from selenium import webdriver
from Shop import ShopPage

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

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_shopping(browser):
    test = ShopPage(browser)

    test.open()
    test.login(USERNAME, PASSWORD)

    for item_name in ITEMS_TO_ADD:
        test.add_item(item_name)

    test.cart()
    test.checkout()
    test.checkout_info(FIRST_NAME, LAST_NAME, ZIP_CODE)

    total_price = test.total_price()
    assert total_price == f"Total: {EXPECTED_TOTAL}", (
        f"Итоговая стоимость не совпадает. Ожидалось: {EXPECTED_TOTAL}, "
        f"Фактически: {total_price}"
    )
