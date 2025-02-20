from selenium import webdriver
from selenium.webdriver.common.by import By

# Open browser
driver = webdriver.Firefox()
driver.get("https://cosmocode.io/automation-practice-webtable/")  # Change to your actual website URL

# Locate the table
table = driver.find_element(By.ID, "countries")

# Find all rows inside tbody
rows = table.find_elements(By.TAG_NAME, "tr")

# Loop through rows
for row in rows:
    # Find all columns (td) inside each row
    cols = row.find_elements(By.TAG_NAME, "td")
    
    # Extract text from each column and print
    row_data = [col.text for col in cols]
    if row_data:  # Avoid printing empty rows
        print(row_data)

# Close the browser
driver.quit()
