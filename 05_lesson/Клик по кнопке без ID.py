from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("http://uitestingplayground.com/dynamicid")

wait = WebDriverWait(driver, 10)
button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary")))
button.click()

driver.quit()
