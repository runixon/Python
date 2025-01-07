from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

for x in range(0, 5):
    button = driver.find_element(By.TAG_NAME, "button")
    button.click()

delete = driver.find_elements(By.CLASS_NAME, "added-manually")
print(f"Количество кнопок 'Delete': {len(delete)}")

driver.quit()