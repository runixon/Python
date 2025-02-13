from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ShopPage:
    """
    Page Object для работы с интернет-магазином.
    """

    def __init__(self, driver):
        """
        Конструктор класса. Инициализирует экземпляр класса ShopPage с переданным драйвером браузера.

        :param driver: Экземпляр WebDriver для управления браузером.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        """
        Открывает главную страницу интернет-магазина.
        """
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username, password):
        """
        Выполняет вход в систему с указанными учетными данными.

        :param username: Логин пользователя.
        :param password: Пароль пользователя.
        """
        self.wait.until(EC.presence_of_element_located((By.ID, "user-name")))
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()

    def add_item(self, item_name):
        """
        Добавляет товар в корзину по его названию.

        :param item_name: Название товара.
        """
        item_xpath = f"//div[text()='{item_name}']/ancestor::div[@class='inventory_item']//button"
        self.wait.until(EC.element_to_be_clickable((By.XPATH, item_xpath)))
        self.driver.find_element(By.XPATH, item_xpath).click()

    def cart(self):
        """
        Переходит на страницу корзины.
        """
        self.driver.get("https://www.saucedemo.com/cart.html")

    def checkout(self):
        """
        Переходит на страницу оформления заказа.
        """
        self.driver.get("https://www.saucedemo.com/checkout-step-one.html")

    def checkout_info(self, first_name, last_name, zip_code):
        """
        Заполняет информацию для оформления заказа.

        :param first_name: Имя покупателя.
        :param last_name: Фамилия покупателя.
        :param zip_code: Почтовый индекс.
        """
        self.wait.until(EC.presence_of_element_located((By.ID, "first-name")))
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(zip_code)
        self.driver.find_element(By.ID, "continue").click()

    def total_price(self):
        """
        Получает итоговую стоимость заказа.

        :return: Текст с итоговой стоимостью.
        :rtype: str
        """
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label")))
        return self.driver.find_element(By.CLASS_NAME, "summary_total_label").text