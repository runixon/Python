import pytest
from selenium import webdriver
from pages.FormPage import FormPage

@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_form_submission(browser):
    form_page = FormPage(browser)
    form_page.open()

    form_page.fill_field("first-name", "Иван")
    form_page.fill_field("last-name", "Петров")
    form_page.fill_field("address", "Ленина, 55-3")
    form_page.fill_field("e-mail", "test@skypro.com")
    form_page.fill_field("phone", "+7985899998787")
    form_page.fill_field("city", "Москва")
    form_page.fill_field("country", "Россия")
    form_page.fill_field("job-position", "QA")
    form_page.fill_field("company", "SkyPro")

    form_page.submit_form()

    assert form_page.is_field_highlighted_red("zip-code"), "Поле Zip code не подсвечено красным"

    fields_to_check = [
        "first-name", "last-name", "address", "e-mail", "phone",
        "city", "country", "job-position", "company"
    ]

    for field_id in fields_to_check:
        assert form_page.is_field_highlighted_green(field_id), f"Поле {field_id} не подсвечено зеленым"