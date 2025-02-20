from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
from selenium.webdriver.common.action_chains import ActionChains
import time

fake = Faker()

driver = webdriver.Firefox()

driver.get("https://collegeinfoweb.netlify.app/")
driver.maximize_window()

wait = WebDriverWait(driver, 10)
actions = ActionChains(driver)
try:

    email = wait.until(EC.presence_of_element_located((By.NAME, "email")))
    password = wait.until(EC.presence_of_element_located((By.NAME, "password")))

    email.send_keys("bibul@abc.com")
    password.send_keys("Admin@123")

    button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Log in']")))
    button.click()

    Affiliation = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text() = ' Affiliation']")))
    Affiliation.click()

    Add_Button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text() = ' Add Affiliation']")))
    Add_Button.click()

    Affiliation_Name = wait.until(EC.presence_of_element_located((By.NAME, "name")))
    actions.move_to_element(Affiliation_Name).click().send_keys(fake.name()).perform()
    time.sleep(2)
    print("Set course name:", Affiliation_Name.get_attribute("value"))

    Website_Link = wait.until(EC.presence_of_element_located((By.NAME, "website_url")))
    Website_Link.send_keys(fake.url())

    Map_Longitude = wait.until(EC.presence_of_element_located((By.NAME, "latitude")))
    Map_Longitude.send_keys(str(fake.latitude()))

    Map_Latitude = wait.until(EC.presence_of_element_located((By.NAME, "longitude")))
    Map_Latitude.send_keys(str(fake.longitude()))

    Established = wait.until(EC.presence_of_element_located((By.NAME, "established_year")))
    Established.send_keys(fake.year())

    Address = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name = 'address']")))
    Address.send_keys(fake.address())

    dropdowns = driver.find_elements(By.XPATH, "//button[@role = 'combobox']")
    dropdowns[0].click()

    District_Option = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text() = 'same']")))
    District_Option.click()

    dropdowns[1].click()
    university_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text() = 'Local']")))
    university_option.click()

    Certificate = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class = 'select__control css-13cymwt-control']")))
    Certificate.click()

    Certificate_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text() = 'Workshop']")))
    Certificate_option.click()

    Phone_Number = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type = 'tel']")))
    Phone_Number.clear()
    time.sleep(2)
    Phone_Number.send_keys(fake.phone_number())

    Email = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type = 'email']")))
    Email.send_keys(fake.email())

    Editor = wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(@data-placeholder,'e.g. Your description goes here...') and contains(@class,'ql-editor')]")))
    Editor.click()
    driver.execute_script("arguments[0].innerHTML = arguments[1]", Editor, fake.text())

    images = driver.find_elements(By.XPATH, "//input[@accept = 'image/*']")
    file = "/home/bebull/Downloads/snak.jpg"

    images[0].send_keys(file)
    images[1].send_keys(file)

    Create = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type = 'submit']")))
    Create.click()
    
except Exception as e:
    print("OOPS something went wrong", e)

