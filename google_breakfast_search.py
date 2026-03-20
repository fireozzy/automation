#!/usr/bin/env python3
"""
Google Breakfast Search Automation
Automates opening Google and searching for "breakfast"
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

def search_google_for_breakfast():
    """Open Google and search for breakfast"""
    
    # Setup Chrome options
    chrome_options = Options()
    # Uncomment the next line to run headless (no visible browser window)
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    
    # Initialize the Chrome driver
    driver = webdriver.Chrome(options=chrome_options)
    
    try:
        print("Opening Google...")
        driver.get("https://www.google.com")
        
        # Wait for page to load
        time.sleep(2)
        
        # Find the search box
        search_box = driver.find_element(By.NAME, "q")
        
        print("Searching for 'breakfast'...")
        search_box.send_keys("breakfast")
        search_box.send_keys(Keys.RETURN)
        
        # Wait to see results
        time.sleep(3)
        
        print("Search complete! Browser will stay open for 10 seconds...")
        time.sleep(10)
        
    finally:
        driver.quit()
        print("Browser closed.")

if __name__ == "__main__":
    search_google_for_breakfast()
