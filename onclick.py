import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time

# Set up the Selenium WebDriver (assuming you're using Chrome)
driver = webdriver.Chrome()

# Set up the headless option
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode
chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration (optional but helpful)
chrome_options.add_argument("--window-size=1920,1080")  # Set window size (optional but useful for some websites)

# Initialize WebDriver with the headless option
driver = webdriver.Chrome(options=chrome_options)



# Open the webpage
driver.get('https://www.bradcot-awnings.co.uk/easyfinder')  # Replace with the actual URL

# Locate the dropdown menu
dropdown = Select(driver.find_element(By.ID, 'step_1_select'))

# Select a manufacturer (e.g., 'ABI')
dropdown.select_by_visible_text('ABI')  # You can also use select_by_value('ABI')

# Optional: Wait for a bit before clicking the next button

# Locate and click the "Next" button
next_button = driver.find_element(By.CLASS_NAME, 'next')

time.sleep(4)

next_button.click()

print('tıkladı1')

# Optional: Wait for a bit to observe the result of clicking "Next"
time.sleep(3)
dropdown2 = Select(driver.find_element(By.ID, 'step_2_select'))
time.sleep(3)

# Select a manufacturer (e.g., 'ABI')
dropdown2.select_by_value('1999')  # You can also use select_by_value('ABI')

# Optional: Wait for a bit before clicking the next button
time.sleep(3)

# Locate and click the "Next" button
next_button2 = driver.find_element(By.CLASS_NAME, 'next')

driver.execute_script("arguments[0].click();", next_button2)

#next_button2.click()

print('tıkladı2')


time.sleep(3)
dropdown3 = Select(driver.find_element(By.ID, 'step_3_select'))
time.sleep(3)

# Select a manufacturer (e.g., 'ABI')
dropdown3.select_by_value('Ace')  # You can also use select_by_value('ABI')

# Optional: Wait for a bit before clicking the next button
time.sleep(3)

# Locate and click the "Next" button
next_button3 = driver.find_element(By.CLASS_NAME, 'next')

driver.execute_script("arguments[0].click();", next_button3)

#next_button2.click()

print('tıkladı3')


time.sleep(3)
dropdown4 = Select(driver.find_element(By.ID, 'step_4_select'))
options = dropdown4.options

# Print the visible text of each option in the dropdown
for option in options:
    print(option.text)


time.sleep(3)

# Select a manufacturer (e.g., 'ABI')
dropdown4.select_by_value('Viceroy')  # You can also use select_by_value('ABI')

# Optional: Wait for a bit before clicking the next button
time.sleep(3)

# Locate and click the "Next" button
next_button4 = driver.find_element(By.CLASS_NAME, 'submit')

driver.execute_script("arguments[0].click();", next_button4)

#next_button2.click()

print('tıkladı4')

time.sleep(3)

#page = driver.page_source
#soup = BeautifulSoup(page,"html.parser")

#print(soup)
# Close the browser
#driver.quit()
