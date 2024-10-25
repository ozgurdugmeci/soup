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

on='url.com'

url_liste=[]


driver = webdriver.Edge()
driver.get(on)  # Replace with the actual URL
time.sleep(1)

search= 'sac yağı'
search_input = driver.find_element(By.CLASS_NAME, "search-box__input")
search_input.send_keys(search)

ara = driver.find_element(By.XPATH, "/html/body/div[1]/header/section[2]/div/div/div[4]/e2-searchbox/v-root/form/div[1]/button[2]")
time.sleep(1)
ara.click()
time.sleep(1)


page = driver.page_source
soup = BeautifulSoup(page,"html.parser")

next_page= soup.find_all('div', class_='paging')
next_page= next_page[0]
next_page=next_page.find_all('e2-plp-page-selectors')

dummy=[]
esas=[]


for i in next_page:
 linky= i.get('href')
 linky= on+linky
 if linky not in url_liste:
  url_liste.append(linky)

print(url_liste) 
 
i=1 
for url in url_liste :

 driver.get(url)  # Replace with the actual URL
 time.sleep(1)
 page = driver.page_source
 soup = BeautifulSoup(page,"html.parser")
 
 detail1 = soup.find_all('div', class_='product-tile__details-and-price')
 
 for rows in detail1:
  urun= rows.find('h3', class_='seo-content-wrapper')
  urun=urun.text
  fiyat= rows.find('e2-price-badge', class_='price-badge__price')
  fiyat = fiyat.get('price')
  member= rows.find('div', class_='price-badge price-badge--membership')
  if member:
   member= member.find('e2-price-badge', class_='price-badge__price')
   member=member.get('other-prices').strip()
   member= member.replace("'","")
   member= member.replace("[","")
   member= member.replace("]","")
   bas=member.find('"value":')
   son=member.find('}')
   member=member[bas+8:son]
   member=float(member)
  else:
   member='-'
  dummy.append(i)
  dummy.append(urun)  
  dummy.append(fiyat) 
  dummy.append(member) 
  esas.append(dummy) 
  dummy=[]
  i=i+1
  
driver.quit()

df=pd.DataFrame(esas)
df.columns=['No','Urun','Raf_Fiyat','Kampanya_Fiyat'] 
writer = pd.ExcelWriter('watsons.xlsx', engine='xlsxwriter')
df.to_excel(writer,'liste')

writer.close()

