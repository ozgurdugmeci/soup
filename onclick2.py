import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
import pickle

driver = webdriver.Chrome()
driver.get('a-web site')  # Replace with the actual URL
driver.implicitly_wait(10)

#MAnufacturer---------------------

dropdown = Select(driver.find_element(By.ID, 'step_1_select'))

options = dropdown.options

listy=[]
for option in options:
  if option.text != 'Please select':
   listy.append(option.text)

print(listy)



dropdown.select_by_visible_text(listy[0])
#dropdown.select_by_index(3)
time.sleep(10)
manu = driver.find_element(By.XPATH, "/html/body/div/div[6]/form/div/div[1]/div[1]/div[2]/button")
time.sleep(1)
manu.click()
#driver.execute_script("arguments[0].click();", manu)
time.sleep(3)
#year-----------------------------------------------------------------

dropdown = Select(driver.find_element(By.ID, 'step_2_select'))
dropdown.select_by_visible_text('1999')
#dropdown.select_by_index(3)
year = driver.find_element(By.XPATH, "/html/body/div/div[6]/form/div/div[1]/div[2]/div[2]/button")
time.sleep(1)
year.click()
time.sleep(3)

#range----------------------------------------------------------------------

dropdown = Select(driver.find_element(By.ID, 'step_3_select'))
dropdown.select_by_visible_text('Ace')
range = driver.find_element(By.XPATH, "/html/body/div/div[6]/form/div/div[1]/div[3]/div[2]/button")
time.sleep(1)
range.click()

time.sleep(3)

#model -------------------------------------------------------------------------------

dropdown = Select(driver.find_element(By.ID, 'step_4_select'))
dropdown.select_by_visible_text('Diplomat')
range = driver.find_element(By.XPATH, "/html/body/div/div[6]/form/div/div[1]/div[4]/div[2]/button")
time.sleep(1)
range.click()
#/html/body/div/div[6]/form/div/div[2]/div[2]/div/h3
time.sleep(3)
page = driver.page_source
soup = BeautifulSoup(page,"html.parser")
size_div = soup.find('div', class_='awn-size-result')
size = size_div.find('h3').text
print(size)

driver.quit()


quit()
