from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Firefox()
driver.get("https://www.google.com")

print(" Original Window Handle:", driver.current_window_handle)

driver.execute_script("window.open('https://www.bing.com');")
time.sleep(2)  


window_handles = driver.window_handles
print(" All Open Windows:", window_handles)


driver.switch_to.window(window_handles[1])
print(" Switched to:", driver.title)  

time.sleep(2)  

driver.switch_to.window(window_handles[0])
print(" Switched back to:", driver.title)  

time.sleep(3)
driver.quit()
