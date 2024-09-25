import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

linko_sezon= 'some_web_site'	


page = requests.get(linko_sezon)

soup = BeautifulSoup(page.content,"html.parser")



select_element = soup.find('select', id='step_1_select') 

manufacturer=[]

for option in select_element:
 name = option.get_text()  # Get the text inside the <option> tag
 if name not in ['\n','Please select'] : 
  manufacturer.append(name) 
 

print(manufacturer)
