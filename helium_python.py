from helium import *
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
url='https://www.tesla.com'
# url='https://quotes.toscrape.com/js/'
browser=start_chrome(url,headless=True)

soup=BeautifulSoup(browser.page_source,'html.parser')
quotes=soup.find_all('a')
print(len(quotes))
# print(quotes)
for quo in quotes:
    # print(quo)
    try:
        new_link = urljoin(url, quo['href'])
        print(new_link)
    except Exception as e:
            pass