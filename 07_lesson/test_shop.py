import pytest
from selenium import webdriver
from pages.ShopPage import LoginPage, InventoryPage, CartPage, CheckoutPage

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

def test_shopping_flow(browser):

    login_page = LoginPage(browser)
    login_page.open()
    login_page.login(USERNAME, PASSWORD)

    inventory_page = InventoryPage(browser)
    for item_name in ITEMS_TO_ADD:
        inventory_page.add_item_to_cart(item_name)

    inventory_page.go_to_cart()

    cart_page = CartPage(browser)
    cart_page.checkout()

    checkout_page = CheckoutPage(browser)
    checkout_page.fill_shipping_info(FIRST_NAME, LAST_NAME, ZIP_CODE)

    total_text = checkout_page.get_total()
    assert total_text == f"Total: {EXPECTED_TOTAL}", (
        f"Итоговая стоимость не совпадает. Ожидалось: {EXPECTED_TOTAL}, "
        f"Фактически: {total_text}"
    )