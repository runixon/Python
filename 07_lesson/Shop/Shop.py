from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ShopPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username, password):
        self.wait.until(EC.presence_of_element_located((By.ID, "user-name")))
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()

    def add_item(self, item_name):
        item_xpath = f"//div[text()='{item_name}']/ancestor::div[@class='inventory_item']//button"
        self.wait.until(EC.element_to_be_clickable((By.XPATH, item_xpath)))
        self.driver.find_element(By.XPATH, item_xpath).click()

    def cart(self):
        self.driver.get("https://www.saucedemo.com/cart.html")

    def checkout(self):
        self.driver.get("https://www.saucedemo.com/checkout-step-one.html")

    def checkout_info(self, first_name, last_name, zip_code):
        self.wait.until(EC.presence_of_element_located((By.ID, "first-name")))
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(zip_code)
        self.driver.find_element(By.ID, "continue").click()

    def total_price(self):
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label")))
        return self.driver.find_element(By.CLASS_NAME, "summary_total_label").text
