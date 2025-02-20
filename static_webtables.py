from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("https://omayo.blogspot.com/")

table = driver.find_element(By.ID, "table1")

rows = table.find_elements(By.TAG_NAME, "tr")

#print("Name"+"     "+"Age"+"    "+"Price")
for row in rows:
    # Get all columns in the current row
    cols = row.find_elements(By.TAG_NAME, "td")
    
    row_data = [col.text for col in cols]
    if row_data: 
        print(row_data)

