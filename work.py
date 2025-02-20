
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import credentials  


driver = webdriver.Firefox() 
driver.implicitly_wait(10)

driver.get("https://www.linkedin.com/login")
time.sleep(2)


email = driver.find_element(By.ID, "username")
email.send_keys("fefawa7090@owlny.com")
pw = driver.find_element(By.ID, "password")
pw.send_keys("Admin@123")

driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(3)

# 6️⃣ Click on the First Job
print("Clicking on the first job listing...")
jobs = driver.find_elements(By.XPATH, "//div[contains(@class, 'job-card-container')]")
if jobs:
    jobs[0].click()  # Click on the first job
    time.sleep(3)
    
    # 7️⃣ Check for "Easy Apply" Button
    print("Checking for 'Easy Apply' button...")
    try:
        apply_button = driver.find_element(By.XPATH, "//button[contains(@class, 'jobs-apply-button')]")
        if apply_button.text == "Easy Apply":
            apply_button.click()
            time.sleep(2)
            
            # 8️⃣ Submit the Application
            print("Submitting application...")
            submit_button = driver.find_element(By.XPATH, "//button[contains(@aria-label, 'Submit application')]")
            submit_button.click()
            print("Applied Successfully!")
            time.sleep(2)
        else:
            print("No 'Easy Apply' button found. Skipping...")
    except:
        print("No 'Easy Apply' option available.")
else:
    print("No jobs found.")

# 9️⃣ Close Browser
print("Closing browser...")
driver.quit()