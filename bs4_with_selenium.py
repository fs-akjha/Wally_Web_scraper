import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
  
#url of the page we want to scrape
url = "https://www.wipro.com/"
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
print(html)
  
# this renders the JS code and stores all
# of the information in static HTML code.
  
# Now, we could simply apply bs4 to html variable
soup = BeautifulSoup(html, "html.parser")
all_divs = soup.find('div')
job_profiles = all_divs.find_all('href')
  
# printing top ten job profiles
count = 0
for job_profile in job_profiles :
    print(job_profile.text)
    count = count + 1
    # if(count == 10) :
    #     break
  
driver.close() # closing the webdriver