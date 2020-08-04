from bs4 import BeautifulSoup
import requests
import re
from selenium import webdriver
import pandas as pd

pd.options.display.float_format = '{:.0f'.format

url = 'https://finance.yahoo.com/quote/MSFT/cash-flow?p=MSFT'
driver = webdriver.Safari()
driver.get(url)
html = driver.execute_script('return document.body.innerHTML;')
soup = BeautifulSoup(html, 'lxml')

price = [entry.text for entry in soup.find_all('span', {'class': 'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'})]
if price != None:
    print('found price')

features = soup.find_all('div', class_ = 'D(tbr)')
if features != None:
    print('found box')

headers = []
temp_list = []
final = []
index = 1

for item in features[0].find_all('div', class_ = 'D(ib)'):
    headers.append(item.text)

while index < len(features):
    temp = features[index].find_all('div', class_ = 'D(tbc)')
    for line in temp:
        temp_list.append(line.text)
    final.append(temp_list)
    temp_list = []
    index += 1

driver.close()
#assert index == 9
df = pd.DataFrame(final)
df.columns = headers 
df.to_csv('MSFT_IS.CSV')