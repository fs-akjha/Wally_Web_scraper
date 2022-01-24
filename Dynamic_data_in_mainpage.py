import requests
from bs4 import BeautifulSoup
import re
import json

response=requests.get('https://quotes.toscrape.com/js')
soup=BeautifulSoup(response.text,"lxml")

scrapt_tag=soup.find("script",src=None)
pattern="var data =(.+?);\n"
raw_data=re.findall(pattern,scrapt_tag.string,re.S)
if raw_data:
    data=json.loads(raw_data[0])

print(data)