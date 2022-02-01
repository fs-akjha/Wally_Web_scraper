import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from urllib.parse import urljoin, urlparse
import time
  
#url of the page we want to scrape
url = "https://www.tesla.com"
chrome_options = Options()
chrome_options.headless = True
chrome_options.add_argument("--headless")
# initiating the webdriver. Parameter includes the path of the webdriver.
driver = webdriver.Chrome(executable_path="./chromedriver.exe", options = chrome_options) 
driver.get(url) 
# driver.find_element_by_css_selector("a[onclick*=DownloadData]").click()
# this is just to ensure that the page is loaded
time.sleep(5) 
  
html = driver.page_source
# this renders the JS code and stores all
# of the information in static HTML code.
  
# Now, we could simply apply bs4 to html variable
soup = BeautifulSoup(html, "html.parser")
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
  
driver.close() # closing the webdriver