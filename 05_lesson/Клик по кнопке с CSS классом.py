from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get(" http://uitestingplayground.com/classattr")

wait = WebDriverWait(driver, timeout=10)
button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")
button.click()

driver.quit()
