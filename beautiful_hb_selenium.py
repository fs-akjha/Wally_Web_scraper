from lib2to3.pgen2 import driver
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions

options=ChromeOptions()
options.headless=True
driver=Chrome(executable_path="./chromedriver.exe",options=options)
driver.get('https://quotes.toscrape.com/page/2/')

soup=BeautifulSoup(driver.page_source,'lxml')
author_element=soup.find_all("small",class_="author")
for i in author_element:
    print(i.text)

driver.quit()