# import libraries
import urllib.request
from bs4 import BeautifulSoup
# specify the url
# urlpage = 'https://groceries.asda.com/search/yogurt' 
# print(urlpage)
# page = urllib.request.urlopen(urlpage)
# soup = BeautifulSoup(page, 'html.parser')
# results = soup.find_all('div', attrs={'class': 'co-product'})
# print('Number of results', len(results))

#With Selenium
import urllib.request
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time
import pandas as pd
# specify the url
urlpage = 'https://groceries.asda.com/search/yogurt' 
print(urlpage)
chrome_options = Options()
chrome_options.add_argument("--headless")
# With headless mode
driver = webdriver.Chrome(executable_path="./chromedriver.exe", options = chrome_options)
# get web page
driver.get(urlpage)
# execute script to scroll down the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
# sleep for 30s
time.sleep(30)
# at time of publication, Nov 2018:
# results = driver.find_elements_by_xpath("//*[@id='componentsContainer']//*[contains(@id,'listingsContainer')]//*[@class='product active']//*[@class='title productTitle']")
# updated Nov 2019:
results = driver.find_elements_by_xpath("//*[@class=' co-product-list__main-cntr']//*[@class=' co-item ']//*[@class='co-product']//*[@class='co-item__title-container']//*[@class='co-product__title']")
print('Number of results', len(results))
data = []
# loop over results
for result in results:
    product_name = result.text
    link = result.find_element_by_tag_name('a')
    product_link = link.get_attribute("href")
    # append dict to array
    data.append({"product" : product_name, "link" : product_link})

df = pd.DataFrame(data)
print(df)
df.to_csv('asdaYogurtLink.csv')
driver.quit()