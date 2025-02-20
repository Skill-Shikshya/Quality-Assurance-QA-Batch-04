from selenium import webdriver


driver = webdriver.Firefox()
driver.get("https://www.google.com")

assert "Google" in driver.title, " Google homepage not loaded!"
print(" Google page title verified!")

"""
assert driver.current_url == "https://www.google.com/", " Wrong URL!"
print(" Google URL is correct")
"""

driver.quit()
