from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/ajax")

blue_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
blue_button.click()

green_banner = WebDriverWait(driver, 20).until(
EC.visibility_of_element_located((By.CSS_SELECTOR, "#content > p"))
)

print(green_banner.text)

driver.quit()
