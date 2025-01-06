from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get("http://the-internet.herokuapp.com/inputs")

wait = WebDriverWait(driver, 10)
input_field = wait.until(EC.presence_of_element_located((By.TAG_NAME, "input")))
input_field.send_keys("1000")
input_field.clear()
input_field.send_keys("999")

driver.quit()
