from lxml import html
import requests
  
# Request the page
page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
  
# Parsing the page
# (We need to use page.content rather than 
# page.text because html.fromstring implicitly
# expects bytes as input.)
tree = html.fromstring(page.content)  
  
# Get element using XPath
buyers = tree.xpath('//a')
print(buyers)