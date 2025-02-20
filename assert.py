from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("https://www.google.com")

wait = WebDriverWait(driver, 10)
search_box = wait.until(EC.presence_of_element_located((By.NAME, "q")))

search_box.send_keys("Selenium Python")
search_box.submit()

wait.until(EC.title_contains("Selenium Python"))

assert "Selenium Python" in driver.title, " Google search failed!"
print(" Google search successful!")

driver.quit()
