import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
flipkart = []
for i in range(1,11):
    url = f'https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.brand%255B%255D%3Drealme&p%5B%5D=facets.availability%255B%255D%3DExclude%2BOut%2Bof%2BStock&param=7564&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIlJlYWxtZSJdLCJ2YWx1ZVR5cGUiOiJNVUxUSV9WQUxVRUQifX19fX0%3D&otracker=clp_metro_expandable_1_5.metroExpandable.METRO_EXPANDABLE_Realme_mobile-phones-store_Q1PDG4YW86MF_wp3&fm=neo%2Fmerchandising&iid=M_6919da7e-40e1-4cd0-b994-6ed921b2fafe_5.Q1PDG4YW86MF&ppt=clp&ppn=mobile-phones-store&ssid=6hvtnzs3kw0000001692383142166{i}'
    html_text = requests.get(url).content
    soup = BeautifulSoup(html_text,'lxml')
    boxes = soup.find_all('a','_1fQZEK')  #['samsung1',samsung2,poco,iphone]
    for box in boxes:
     phone_data = {}
     name = box.find('div','_4rR01T').get_text()
     price = box.find('div','_30jeq3 _1_WHN1').get_text()
     rating = box.find('div','_3LWZlK').get_text()
     phone_data['Name'] = name
     phone_data['Price'] = price
     phone_data['Rating'] = rating
     flipkart.append(phone_data)
df = pd.json_normalize(flipkart)
df.to_excel('Flipkart-Phones.xlsx')