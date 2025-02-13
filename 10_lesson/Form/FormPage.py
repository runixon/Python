from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FormPage:
    """
    Page Object для работы с формой на веб-странице.
    """

    def __init__(self, driver):
        """
        Конструктор класса. Инициализирует экземпляр класса FormPage с переданным драйвером браузера.

        :param driver: Экземпляр WebDriver для управления браузером.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        """
        Открывает страницу с формой.
        """
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    def fill(self, field_name, value):
        """
        Заполняет поле формы указанным значением.

        :param field_name: Имя поля (атрибут `name`).
        :param value: Значение, которое нужно ввести в поле.
        """
        self.wait.until(EC.presence_of_element_located((By.NAME, field_name)))
        self.driver.find_element(By.NAME, field_name).send_keys(value)

    def submit(self):
        """
        Нажимает кнопку отправки формы.
        """
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    def is_green(self, field_name):
        """
        Проверяет, подсвечено ли поле зеленым цветом (успешная валидация).

        :param field_name: Имя поля (атрибут `id`).
        :return: True, если поле подсвечено зеленым, иначе False.
        """
        field = self.driver.find_element(By.ID, field_name)
        result = "alert-success" in field.get_attribute("class")
        print(f"Field {field_name} is green: {result}")
        return result

    def is_red(self, field_name):
        """
        Проверяет, подсвечено ли поле красным цветом (ошибка валидации).

        :param field_name: Имя поля (атрибут `id`).
        :return: True, если поле подсвечено красным, иначе False.
        """
        field = self.driver.find_element(By.ID, field_name)
        result = "alert-danger" in field.get_attribute("class")
        print(f"Field {field_name} is red: {result}")
        return result