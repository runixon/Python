import pytest
from selenium import webdriver
from pages.CalcPage import CalcPage

@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_slow_calculator(browser):
    calculator_page = CalcPage(browser)
    calculator_page.open()

    calculator_page.set_delay("45")

    calculator_page.click_button("7")
    calculator_page.click_button("+")
    calculator_page.click_button("8")
    calculator_page.click_button("=")

    result = calculator_page.get_result(45)
    assert result == "15", "Результат на экране не равен 15"