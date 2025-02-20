from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("https://www.techlistic.com/2017/02/automate-demo-web-table-with-selenium.html")
table = driver.find_element(By.XPATH, "//table[@id = 'customers']")

headers = driver.find_elements(By.XPATH, "//table/tbody/tr[1]/th")
header_texts = [header.text for header in headers]
print("\n Table Headers:", "   ".join(header_texts))

rows = table.find_elements(By.XPATH, "//table/tbody/tr[position()>1]")

print("\n Table Data:")
for row in rows:

    cols = row.find_elements(By.TAG_NAME, "td")
    
    row_data = [col.text for col in cols]
    print("    ".join(row_data))


driver.quit()
