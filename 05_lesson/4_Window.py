from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/entry_ad")

wait = WebDriverWait(driver, 10)
close_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.modal-footer > p")))
close_button.click()

driver.quit()
