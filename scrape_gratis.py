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

on='https://www.gratis.com/'

url_liste=[]


driver = webdriver.Edge()
driver.get(on)  # Replace with the actual URL
time.sleep(3)

try:
 ara = driver.find_element(By.CLASS_NAME, "popup_close")
 
 time.sleep(1)
 ara.click()
 time.sleep(1)
except:
 pass

search= 'kondom'
search_input = driver.find_element(By.CLASS_NAME, "search-input")
time.sleep(1)
search_input.send_keys(search)
time.sleep(1)



#ara = driver.find_element(By.XPATH, "//span[@class='typeahead__button']/button")
time.sleep(6)

page = driver.page_source
soup = BeautifulSoup(page,"html.parser")
dummy=[]
esas=[]
i=0
parca = soup.find_all('div', class_='sgm-search-product-info')
for row in parca:
 i=i+1
 namo= row.find('div', class_='sgm-search-product-info-name') 
 current_price= row.find('div', class_='sgm-current-price')
 namo=namo.text
 current_price=current_price.text.split()
 current_price=current_price[0]
 dummy.append(i)
 dummy.append(namo)
 dummy.append(current_price)
 esas.append(dummy)
 dummy=[]
driver.quit()



df=pd.DataFrame(esas)
df.columns=['No','Urun','Guncel_Fiyat'] 
writer = pd.ExcelWriter('gratis.xlsx', engine='xlsxwriter')
df.to_excel(writer,'liste')

writer.close()

