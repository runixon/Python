import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
    # Шаг 1: Открыть сайт магазина
    browser.get("https://www.saucedemo.com/")

    username_field = browser.find_element(By.ID, "user-name")
    password_field = browser.find_element(By.ID, "password")
    login_button = browser.find_element(By.ID, "login-button")

    username_field.send_keys(USERNAME)
    password_field.send_keys(PASSWORD)
    login_button.click()

    for item_name in ITEMS_TO_ADD:
        item_xpath = (
            f"//div[text()='{item_name}']/ancestor::div[@class='inventory_item']//button"
        )
        add_to_cart_button = browser.find_element(By.XPATH, item_xpath)
        add_to_cart_button.click()

    cart_button = browser.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart_button.click()

    checkout_button = browser.find_element(By.ID, "checkout")
    checkout_button.click()

    first_name_field = browser.find_element(By.ID, "first-name")
    last_name_field = browser.find_element(By.ID, "last-name")
    zip_code_field = browser.find_element(By.ID, "postal-code")
    continue_button = browser.find_element(By.ID, "continue")

    first_name_field.send_keys(FIRST_NAME)
    last_name_field.send_keys(LAST_NAME)
    zip_code_field.send_keys(ZIP_CODE)
    continue_button.click()

    total_label = browser.find_element(By.CLASS_NAME, "summary_total_label")
    total_text = total_label.text

    assert total_text == f"Total: {EXPECTED_TOTAL}", (
        f"Итоговая стоимость не совпадает. Ожидалось: {EXPECTED_TOTAL}, "
        f"Фактически: {total_text}"
    )