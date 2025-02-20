from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
import time
from selenium.webdriver.common.action_chains import ActionChains


fake = Faker()

driver = webdriver.Firefox()

driver.get("https://collegeinfoweb.netlify.app/")
driver.maximize_window()
actions = ActionChains(driver)
wait = WebDriverWait(driver, 20)  
try:
    
    email = wait.until(EC.visibility_of_element_located((By.NAME, "email")))
    password = wait.until(EC.visibility_of_element_located((By.NAME, "password")))

    email.send_keys("admin123@gmail.com")
    password.send_keys("admin")

    button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Log in']")))
    button.click()

    Social_Media = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[text() = ' Social Media']")))
    Social_Media.click()

    Add = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Add Social Media ']")))
    Add.click()

    Name = wait.until(EC.presence_of_element_located((By.NAME, "name")))
    actions.move_to_element(Name).click().send_keys(fake.random_lowercase_letter()).perform()
    time.sleep(2)

    Link = wait.until(EC.presence_of_element_located((By.NAME, "link")))
    actions.move_to_element(Link).click().send_keys(fake.url()).perform()

    Image = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@accept = 'image/*']")))
    file = "/home/bebull/Downloads/Mask group.png"
    Image.send_keys(file)

    Create = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@value = 'Create']")))
    Create.click()
    time.sleep(3)
except Exception as e:
    print("Hey you done sthg wrong ", e)
finally:
    driver.quit()