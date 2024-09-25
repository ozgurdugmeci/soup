import requests
from bs4 import BeautifulSoup
import pandas as pd
import json


linko_sezon= 'somewebsite'	


page = requests.get(linko_sezon)

soup = BeautifulSoup(page.content,"html.parser")




kk =soup.find_all('a', class_='sub-menu-item')
#kk =soup.find_all('div', class_='right')


liste=[]

for item in kk:
 url = item.get('href')  # Extract the URL from the 'href' attribute
 
 text = item.get_text()   # Extract the text inside the <a> tag
 texto= f"Sub-menu text: {text}, URL: {url}"
 liste.append(texto)
 
liste=pd.DataFrame(liste) 
liste.columns=['Text']

print(liste)

quit()


writer = pd.ExcelWriter('karavan2.xlsx', engine='xlsxwriter')
liste.to_excel(writer,'Etiketleme_OOS_Analiz')

writer.close()	







