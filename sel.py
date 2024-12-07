from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

# Provide the correct path to your ChromeDriver
chrome_service = Service("C:\Program Files\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_service)

try:
    # Open Google
    driver.get("https://www.google.com")
    
    # Find the search box and search for the given URL
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("https://cmrcet.ac.in/")
    search_box.send_keys(Keys.RETURN)
    
    # Wait for the results to load
    time.sleep(20)
finally:
    # Quit the browser
    driver.quit()