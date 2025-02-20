from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("https://omayo.blogspot.com/")

table = driver.find_element(By.ID, "table1")
headers = table.find_elements(By.TAG_NAME, "th")


for header in headers:
    print(header.text, end="  ")  
print("\n" + "-" * 30) 


rows = table.find_elements(By.TAG_NAME, "tr")

for row in rows:
    datas = row.find_elements(By.TAG_NAME, "td")
  
    for data in datas:
        print(data.text, end="  ")  

    print()  
driver.quit()
