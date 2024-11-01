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

#https://www.carrefoursa.com/search/?text=deterjan%3Arelevance&page=10
#https://www.carrefoursa.com/search?q=deterjan%3Arelevance&page=10
on='https://www.carrefoursa.com/search/?text='
iki='https://www.carrefoursa.com/search?q='
search= 'deterjan'
link=on+search
url_liste=[]


driver = webdriver.Edge()
driver.get(link)  # Replace with the actual URL
time.sleep(4)

dummy=[]
esas=[]
page = driver.page_source
soup = BeautifulSoup(page,"html.parser")

parca= soup.find_all('li', class_='product-listing-item')

r=1
for row in parca:
 parcax=row.find('h3','item-name')
 namo= parcax.text
 print(namo)
 parcax=row.find('div','item-price-contain')
 raf_fiyat=parcax.find('span','priceLineThrough js-variant-price')
 if raf_fiyat:
  raf_fiyat=raf_fiyat.text
  raf_fiyat=raf_fiyat.split()
  raf_fiyat=raf_fiyat[0]
  print(raf_fiyat)
 else:
  raf_fiyat='-' 
 kamp_fiyat=parcax.find('span','item-price js-variant-discounted-price')
 if kamp_fiyat:
  kamp_fiyat=kamp_fiyat.get('content').split()
  kamp_fiyat=kamp_fiyat[0]
  print(kamp_fiyat)
 else:
  kamp_fiyat='-'
 dummy.append(r)
 dummy.append(namo)
 dummy.append(raf_fiyat)
 dummy.append(kamp_fiyat)
 esas.append(dummy)
 dummy=[]
 r=r+1
  
search2='%3Arelevance&page=' 
i=2
pagy=str(i)
  
while i<=10  :
 link=iki+search+search2+pagy
 driver.get(link)  # Replace with the actual URL
 time.sleep(4)


 page = driver.page_source
 soup = BeautifulSoup(page,"html.parser")
 
 parca= soup.find_all('li', class_='product-listing-item')
 
 for row in parca:
  parcax=row.find('h3','item-name')
  namo= parcax.text
  print(namo)
  parcax=row.find('div','item-price-contain')
  raf_fiyat=parcax.find('span','priceLineThrough js-variant-price')
  if raf_fiyat:
   raf_fiyat=raf_fiyat.text
   raf_fiyat=raf_fiyat.split()
   raf_fiyat=raf_fiyat[0]
   print(raf_fiyat)
  else:
   raf_fiyat='-'  
  kamp_fiyat=parcax.find('span','item-price js-variant-discounted-price')
  if kamp_fiyat:
   kamp_fiyat=kamp_fiyat.get('content').split()
   kamp_fiyat=kamp_fiyat[0]
   print(kamp_fiyat)
  else:
   kamp_fiyat='-'  
  r=r+1 
  dummy.append(r)
  dummy.append(namo)
  dummy.append(raf_fiyat)
  dummy.append(kamp_fiyat)
  esas.append(dummy)
  dummy=[] 
 i=i+1
 pagy=str(i) 
 

driver.quit()

df=pd.DataFrame(esas)
df.columns=['No','Urun','Raf_Fiyat','Kampanya_Fiyat'] 
writer = pd.ExcelWriter('carrefour.xlsx', engine='xlsxwriter')
df.to_excel(writer,'liste')

writer.close()

