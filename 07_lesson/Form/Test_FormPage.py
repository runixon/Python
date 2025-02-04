import pytest
from selenium import webdriver
from FormPage import FormPage

@pytest.fixture

def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_form_submission(driver):
    test = FormPage(driver)

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

    for field_name, value in form_data.items():
        test.fill(field_name, value)

    test.submit()

    assert test.is_red("zip-code")

    for field_name in form_data.keys():
        assert test.is_green(field_name)
