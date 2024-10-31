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

on='https://www.eveshop.com.tr/search?type=product&q='
iki='https://www.eveshop.com.tr'
search= 'şampuan'
link=on+search
url_liste=[]


driver = webdriver.Edge()
driver.get(link)  # Replace with the actual URL
time.sleep(1)


page = driver.page_source
soup = BeautifulSoup(page,"html.parser")

#parca= soup.find('section', id='PageContainer')
parca= soup.find_all('div', class_='product--item col-xl-3 col-lg-3 col-md-4 col-sm-6 col-xs-6 mg-5 mb-20')
i=1
dummy=[]
esas=[]
for row in parca:
 #parcax= row.find('div', class_='product__info')
 parcax= row.find('div','product__title')
 namo=parcax.text
 parcax= row.find('div','product-price__price')
 
 raf_fiyat=parcax.text
 raf_fiyat=raf_fiyat.split()
 raf_fiyat=raf_fiyat[0]
 #listingPriceNormal undefined
 parcax= row.find('div','listingPriceNormal undefined')
 try:
  kart_fiyat=parcax.text
  kart_fiyat=kart_fiyat.split()
  kart_fiyat=kart_fiyat[3]
 except:
  kart_fiyat=('-') 
 
 dummy.append(i)
 dummy.append(namo)
 dummy.append(raf_fiyat)
 dummy.append(kart_fiyat)
 esas.append(dummy)
 dummy=[]
 i=i+1
 
#1 bilgileri al
loop=0

next_page= soup.find('a', id='loadMore')
next_page= next_page.get('href')
link=iki+next_page

#2 loop' a gir eğer sonraki sayfa yoksa loop'tan çık
while loop == 0 :
 driver.get(link)  # Replace with the actual URL
 time.sleep(1)
 page = driver.page_source
 soup = BeautifulSoup(page,"html.parser")

 parca= soup.find_all('div', class_='product--item col-xl-3 col-lg-3 col-md-4 col-sm-6 col-xs-6 mg-5 mb-20')
 for row in parca:
  #parcax= row.find('div', class_='product__info')
  parcax= row.find('div','product__title')
  namo=parcax.text
  parcax= row.find('div','product-price__price')
  
  raf_fiyat=parcax.text
  raf_fiyat=raf_fiyat.split()
  raf_fiyat=raf_fiyat[0]
  #listingPriceNormal undefined
  parcax= row.find('div','listingPriceNormal undefined')
  try:
   kart_fiyat=parcax.text
   kart_fiyat=kart_fiyat.split()
   kart_fiyat=kart_fiyat[3]
  except:
   kart_fiyat=('-') 
  
  dummy.append(i)
  dummy.append(namo)
  dummy.append(raf_fiyat)
  dummy.append(kart_fiyat)
  esas.append(dummy)
  dummy=[]
  i=i+1
  next_page= soup.find('a', id='loadMore')
  if next_page:
   next_page= next_page.get('href')
   link=iki+next_page
  else:
   loop=2
   break   


  
driver.quit()

df=pd.DataFrame(esas)
df.columns=['No','Urun','Raf_Fiyat','Kampanya_Fiyat'] 
writer = pd.ExcelWriter('eve.xlsx', engine='xlsxwriter')
df.to_excel(writer,'liste')

writer.close()

