import pytest
from selenium import webdriver
from Calculator import Calc

@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_slow_calculator(browser):
    test = Calc(browser)

    test.open()
    test.set_delay("45")  # Устанавливаем задержку 45 секунд

    test.click_button("7")
    test.click_button("+")
    test.click_button("8")
    test.click_button("=")

    result = test.get_result()

    assert result == "15", "Результат на экране не равен 15"
