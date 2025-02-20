from playwright.sync_api import sync_playwright
from faker import Faker
import time

fake = Faker()

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # Navigate to the website
    page.goto("https://collegeinfoweb.netlify.app/")
    page.set_viewport_size({"width": 1366, "height": 768})

    # Fill login details and log in
    page.fill("[name='email']", "admin123@gmail.com")
    page.fill("[name='password']", "admin")
    page.click("//button[text() = 'Log in']")
    
    # Wait for the Add Course button to be clickable
    page.wait_for_selector("//button[text() = 'Add Course']", state='visible')
    page.click("//button[text() = 'Add Course']")

    # Fill out the course details
    page.fill("//input[@placeholder = 'e.g. Bachelors of Business Management']", fake.name())
    page.fill("[name='abbreviation']", "ABCD")

    # Wait for the comboboxes to be visible and click them
    page.wait_for_selector('button[role="combobox"]', state='visible')
    page.click('button[role="combobox"]')
    page.click("//div[text() = 'test affiliation']")
    
    page.wait_for_selector('button[role="combobox"]:nth-of-type(2)', timeout=60000)  # 60 seconds
    page.click('button[role="combobox"]:nth-of-type(2)')
    page.click("//div[text() = 'awdawd']")
    
    page.wait_for_selector('button[role="combobox"]:nth-of-type(3)', state='visible')
    page.click('button[role="combobox"]:nth-of-type(3)')
    page.click("//div[text() = 'Engineering']")
    
    page.wait_for_selector('button[role="combobox"]:nth-of-type(4)', state='visible')
    page.click('button[role="combobox"]:nth-of-type(4)')
    page.click("//*[text() = 'Bachelors']")
    
    # Select the supreme update option
    page.wait_for_selector("//div[@class = 'select__input-container css-19bb58m']", state='visible')
    page.click("//div[@class = 'select__input-container css-19bb58m']")
    page.click("//div[text() = 'supreme update ok']")

    # Fill in the Quill editor fields with fake text
    quill_editors = page.query_selector_all("div.ql-editor")
    for editor in quill_editors:
        editor.click()
        page.evaluate("arguments[0].innerHTML = arguments[1]", editor, fake.text())

    # Handle image uploads
    img_input = page.query_selector_all("//input[@accept = 'image/*']")
    file = "/home/bebull/Downloads/Mask group.png"

    if img_input:
        img_input[0].set_input_files(file)
        img_input[1].set_input_files(file)

    # Wait for the final button to be visible and then click to submit the form
    page.wait_for_selector("//button[text() = 'Add Course']", state='visible')
    page.click("//button[text() = 'Add Course']")

    # Close the browser after the task is done
    browser.close()
