import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time

on='https://www.rossmann.com.tr/catalogsearch/result/?q='
iki='https://www.rossmann.com.tr/'
search= 'şampuan'
link=on+search


driver = webdriver.Edge()
driver.get(link)  # Replace with the actual URL
time.sleep(2)

driver.get(link)  # Replace with the actual URL
time.sleep(2)

for _ in range(8):
 driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
 time.sleep(2)  # Pause to let content load if necessary




page = driver.page_source
soup = BeautifulSoup(page,"html.parser")


'''driver.execute_script("window.scrollBy(0, 1000);")
time.sleep(2)  # Pause if needed'''

#parca= soup.find('section', id='PageContainer')
parca= soup.find_all('div', class_='product-item-info')

i=1
dummy=[]
esas=[]
for row in parca:
 
 parcax=row.find('strong', class_='product brand product-item-name')
 marka=parcax.text
 marka=marka.split()
 marka=marka[0]
 parcax=row.find('strong', class_='product name product-item-name')
 namo=parcax.text
 namo=namo.split()
 namo=' '.join(namo)
 namo= marka+ '-' + namo
 
 parcax=row.find('div', class_='price-box price-final_price')
 
 try:
  parcax=parcax.find('span', class_='price mobilePrice')
  raf_fiyat= parcax.text
 except:
  parcax=row.find('div', class_='price-box price-final_price')
  parcax=parcax.find('span', class_='regular-price')
  parcax=parcax.find('span', class_='price')
  raf_fiyat=parcax.text
  print(namo)
  print(raf_fiyat)
  
 try:
  parcax=row.find('div', class_='mobilePriceFlex')
  parcax=parcax.find('span', class_='price')
  kart_fiyat= parcax.text
 except:
  try:
   parcax=row.find('div', class_='cart-campaign-wrapper color-lipstick-red')
   parcax=parcax.find('div', class_='cart-campaign-price text-right')
   kart_fiyat= parcax.text
  except:
   kart_fiyat='-'
  
 dummy.append(i)
 dummy.append(namo)
 dummy.append(raf_fiyat)
 dummy.append(kart_fiyat)
 esas.append(dummy)
 dummy=[]
 i=i+1
 

 
driver.quit()

df=pd.DataFrame(esas)
df.columns=['No','Urun','Raf_Fiyat','Kampanya_Fiyat'] 
writer = pd.ExcelWriter('ross.xlsx', engine='xlsxwriter')
df.to_excel(writer,'liste')

writer.close()

