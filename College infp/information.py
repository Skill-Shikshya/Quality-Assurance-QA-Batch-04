from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from faker import Faker
from selenium.webdriver.common.action_chains import ActionChains

fake = Faker()
driver = webdriver.Firefox()
driver.get("https://collegeinfoweb.netlify.app/")
driver.maximize_window()

wait = WebDriverWait(driver, 15)

email = wait.until(EC.presence_of_element_located((By.NAME, "email")))
password = wait.until(EC.presence_of_element_located((By.NAME, "password")))
email.send_keys("bibul@gmail.com")
password.send_keys("bibul")
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Log in']"))).click()

wait.until(EC.element_to_be_clickable((By.XPATH, "//li[contains(text(), 'Information')]"))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Add Information']"))).click()

Title = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name = 'title']")))
Title.send_keys(fake.name())

slug = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name = 'slug']")))
slug.send_keys(fake.random_lowercase_letter())

Date_Picker = driver.find_elements(By.XPATH, "(//span[text() = 'Pick a date'])")


Date_Picker[1].click()
left_side = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@name = 'day'])[32]")))
left_side.click()

right_side = wait.until(EC.presence_of_element_located((By.XPATH, "(//button[@name = 'day'])[57]")))
right_side.click()

dropdowns = driver.find_elements(By.XPATH, "//input[@class = 'select__input']")
dropdowns[0].click()

level_option = wait.until(EC.presence_of_element_located((By.XPATH, "//div[text() = 'test']")))
level_option.click()

dropdowns[1].click()
college_option = wait.until(EC.presence_of_element_located((By.XPATH, "//div[text() = 'Uniglobe College']")))
college_option.click()
time.sleep(3)

dropdowns[2].click()
course_option = wait.until(EC.presence_of_element_located((By.XPATH, "//div[text() = 'Bachelor in Administration']")))
course_option.click()

dropdowns[3].click()
affiliation_option = wait.until(EC.presence_of_element_located((By.XPATH, "//div[text() = 'Pokhara University']")))
affiliation_option.click()

dropdowns[4].click()
faculty_option = wait.until(EC.presence_of_element_located((By.XPATH, "//div[text() = 'Humanities']")))
faculty_option.click()

dropdowns[5].click()
district_option = wait.until(EC.presence_of_element_located((By.XPATH, "//div[text() = 'Kathmandu']")))
district_option.click()

dropdowns[6].click()
tags_option = wait.until(EC.presence_of_element_located((By.XPATH, "//div[text() = 'Execursion']")))
tags_option.click()

dropdowns[7].click()
categories_option = wait.until(EC.presence_of_element_located((By.XPATH, "//div[text() = 'Exam']")))
categories_option.click()

editors = driver.find_elements(By.XPATH, "//div[@class = 'ql-container ql-snow']")

for editor in editors:
    editor.click()
    driver.execute_script("arguments[0].innerHTML = arguments[1]", editor, fake.text())


Upload_image = driver.find_element(By.XPATH, "//input[@accept = 'image/*']")
file = "/home/bebull/Downloads/Mask group.png"
Upload_image.send_keys(file)

Upload_Document = driver.find_element(By.XPATH, "//input[@id = 'file-upload']")
Upload_Document.send_keys(file)

Add_Info = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Add Information']")))
Add_Info.click()

