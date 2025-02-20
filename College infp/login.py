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

wait = WebDriverWait(driver, 20)  
try:
    abc = driver.get_cookies()
    print(abc)
    email = wait.until(EC.visibility_of_element_located((By.NAME, "email")))
    password = wait.until(EC.visibility_of_element_located((By.NAME, "password")))

    email.send_keys("bibul@gmail.com")
    password.send_keys("bibul")

    button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Log in']")))
    button.click()

    add_course = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Add Course']")))
    add_course.click()

    course_name_input = wait.until(EC.presence_of_element_located((By.NAME, "name")))
    fake_course_name = fake.name()
    driver.execute_script("arguments[0].click();", course_name_input)
    course_name_input.clear()
    actions = ActionChains(driver)
    actions.move_to_element(course_name_input).click().send_keys(fake_course_name).perform()
    time.sleep(2)
    print("Set course name:", course_name_input.get_attribute("value"))

   
    Abbreviation = wait.until(EC.visibility_of_element_located((By.NAME, "abbreviation")))
    Abbreviation.send_keys(fake.random_uppercase_letter())

    dropdowns = driver.find_elements(By.CSS_SELECTOR, 'button[role="combobox"]')
    dropdowns[0].click()
    affiliation_value = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text() = 'Bachelor of Science in Computer Science']")))
    affiliation_value.click()

    dropdowns[1].click()
    duration_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text() = 'awdawd']")))
    duration_option.click()

    dropdowns[2].click()
    faculties_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text() = 'Engineering']")))
    faculties_option.click()

    dropdowns[3].click()
    level_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text() = 'test']")))
    level_option.click()

    Discipline = driver.find_element(By.XPATH, "//div[@class = 'select__input-container css-19bb58m']")
    Discipline.click()

    discipline_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text() = 'fggfg']")))
    discipline_option.click()

    quill_editors = driver.find_elements(By.CSS_SELECTOR, "div.ql-editor")
    for editor in quill_editors:
        editor.click()
        driver.execute_script("arguments[0].innerHTML = arguments[1]", editor, fake.text())

    img_input = driver.find_elements(By.XPATH, "//input[@accept = 'image/*']")
    file = "/home/bebull/Downloads/Mask group.png"
    
    wait.until(EC.element_to_be_clickable(img_input[0]))
    img_input[0].send_keys(file)

    Upload_Document = driver.find_element(By.XPATH, "//input[@id = 'file-upload']")
    Upload_Document.send_keys(file)
    time.sleep(3)
    create_course = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Add Course']")))
    create_course.click()

    Notice = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Course Successfully Created')]")))
    Not_message = Notice.text.strip()

    expected_text = "Course Not Successfully Created".strip()
    assert expected_text in Not_message, f"Expected: {expected_text} but got {Not_message}"
    print(Not_message)
except Exception as e:
    print("Something is wrong:", e)
    

    """success_toast = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "toaster group")))  
    success_message = success_toast.text

    for request in driver.requests:
        print(request.url)  
   
    request_found = False  

    for request in driver.requests:
        if "addCourse" in request.url and request.response:
            status_code = request.response.status_code
            assert status_code in [200, 201], f" Course creation failed! HTTP Status: {status_code}"
            print(f" Course successfully created! HTTP Status: {status_code}")
            request_found = True
            break

    if not request_found:
        print(" No API response found for course creation!")
"""
    

    
