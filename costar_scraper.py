from bs4 import BeautifulSoup
import requests
#import lxml.html

# Url to scrape
try:
    my_url = requests.get('https://www.loopnet.com/Listing/1317-State-St-Salem-OR/18758497/', timeout=10, verify =False).text
#session =  HTMLSession()
#result = session.get(my_url)  #Opens the url

#src = result.content
    soup = BeautifulSoup(my_url, 'html.parser')

#print(result.text[:500])
    urls = []
#print(soup.prettify())

    print_this = soup.find('div',{'id': 'available-spaces'})
    if print_this != None:
        print(worked)
except:
    print('errors')

"""
if print_this is not None:
    name = print_this.text
else: 
    name = 'didnt work'
print(name)
"""

"""
dfdfhdfdfhdf
"""