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

#https://www.migros.com.tr/arama?q=deterjan&sayfa=2&sirala=akilli-siralama

on='https://www.migros.com.tr/arama?q='

ek='&sirala=akilli-siralama'
#link=iki+pagy+ek
search= 'deterjan'
iki=on+search+'&sayfa='
link=on+search
url_liste=[]


driver = webdriver.Edge()
driver.get(link)  # Replace with the actual URL
time.sleep(4)


dummy=[]
esas=[]
page = driver.page_source
soup = BeautifulSoup(page,"html.parser")



parca= soup.find('div', class_='mdc-layout-grid__inner product-cards list ng-star-inserted')
#                               mdc-layout-grid__inner product-cards list ng-star-inserted






parca=parca.find_all('sm-list-page-item',class_='mdc-layout-grid__cell--span-2-desktop mdc-layout-grid__cell--span-4-tablet mdc-layout-grid__cell--span-2-phone ng-star-inserted')
#sm-list-page-item
r=1
for row in parca:
 parcax=row.find('a',id='product-name')
 namo= parcax.text
 print(namo)
 
 parcax=row.find('div',class_='price-new subtitle-1 ng-star-inserted')
 
 if parcax:
  raf_fiyat=parcax.text
 else:
  raf_fiyat='-'
 print(raf_fiyat) 
 parcax=row.find('div',class_='unit-price ng-star-inserted')
 if parcax:
  birim_fiyat=parcax.text 
 else:
  birim_fiyat='-' 
 print(birim_fiyat)
 parcax=row.find('span',class_='single-price-amount')
 if parcax:
  single_price=parcax.text
 else:
  single_price='-'
 print(single_price)
 parcax=row.find('div',class_='price mat-caption-bold')
 if parcax:
  money_card=parcax.text
 else:
  money_card='-'
 print(money_card)
 dummy.append(r)
 dummy.append(namo)
 dummy.append(raf_fiyat)
 dummy.append(single_price)
 dummy.append(money_card)
 dummy.append(birim_fiyat)
 esas.append(dummy)
 dummy=[]
 r=r+1


i=2
pagy=str(i)







  
while i<=20  :
 link=iki+pagy+ek
 driver.get(link)  # Replace with the actual URL
 time.sleep(4)


 page = driver.page_source
 soup = BeautifulSoup(page,"html.parser")
 parca= soup.find('div', class_='mdc-layout-grid__inner product-cards list ng-star-inserted')
 #                               mdc-layout-grid__inner product-cards list ng-star-inserted

 if parca:
  parca=parca.find_all('sm-list-page-item',class_='mdc-layout-grid__cell--span-2-desktop mdc-layout-grid__cell--span-4-tablet mdc-layout-grid__cell--span-2-phone ng-star-inserted')
  #sm-list-page-item

  for row in parca:
   parcax=row.find('a',id='product-name')
   namo= parcax.text
   print(namo)
   
   parcax=row.find('div',class_='price-new subtitle-1 ng-star-inserted')
   
   if parcax:
    raf_fiyat=parcax.text
   else:
    raf_fiyat='-'
   print(raf_fiyat) 
   parcax=row.find('div',class_='unit-price ng-star-inserted')
   if parcax:
    birim_fiyat=parcax.text 
   else:
    birim_fiyat='-' 
   print(birim_fiyat)
   parcax=row.find('span',class_='single-price-amount')
   if parcax:
    single_price=parcax.text
   else:
    single_price='-'
   print(single_price)
   parcax=row.find('div',class_='price mat-caption-bold')
   if parcax:
    money_card=parcax.text
   else:
    money_card='-'
   print(money_card)
   dummy.append(r)
   dummy.append(namo)
   dummy.append(raf_fiyat)
   dummy.append(single_price)
   dummy.append(money_card)
   dummy.append(birim_fiyat)
   esas.append(dummy)
   dummy=[]
   r=r+1
 
  i=i+1
  pagy=str(i)  
 else:
  break
  i=1000
driver.quit()

df=pd.DataFrame(esas)
df.columns=['No','Urun','Raf_Fiyat','Single_Price','Money_Card_Fiyat','Birim_Fiyat'] 
writer = pd.ExcelWriter('migros.xlsx', engine='xlsxwriter')
df.to_excel(writer,'liste')

writer.close()

