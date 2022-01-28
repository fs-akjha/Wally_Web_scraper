# testing JS containing pages
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
url='https://www.tesla.com'
# url='https://quotes.toscrape.com/js/'
r=requests.get(url)
# print(r.text)
soup=BeautifulSoup(r.text,'html.parser')
quotes=soup.find_all('a')
print(len(quotes))
for quo in quotes:
    # print(quo)
    try:
        new_link = urljoin(url, quo['href'])
        print(new_link)
    except Exception as e:
            pass