from bs4 import BeautifulSoup
import requests
import pandas as pd

url = requests.get('https://finance.yahoo.com/quote/GOOG?p=GOOG').text
soup = BeautifulSoup(url, 'html.parser')

alldata = soup.find_all("tbody")
try:
    table1 = alldata[0].find_all("tr")
    print("table1 successful")
except:
    table1 = None

try: 
    table2 = alldata[1].find_all("tr")
    print("table2 successful")
except:
    table2 = None


liss = {}
dic = list()

check = 'bid'
count = 0
for i in range(0, len(table1)):
    try:
        table1_td = table1[i].find_all("td")
    except:
        table1_td = None
    
    liss[table1_td[0].text] = table1_td[1].text

    dic.append(liss)
    liss = {}

for i in range(0, len(table2)):
    try:
        table2_td = table2[i].find_all("td")
    except:
        table2_td = None
    
    liss[table2_td[0].text] = table2_td[1].text

    dic.append(liss)
    liss = {}

#print_dic = {dic}

#apple_scrape_df = pd.DataFrame.from_dict(dic)
#apple_scrape_df.to_csv('apple_scrape.csv')
print(dic)
