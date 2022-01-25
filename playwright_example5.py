from playwright.sync_api import sync_playwright
import datetime
import re
import pandas as pd


def retrieve_county(county, page):

  # navigate to county-specific page
  county_url = county.lower().replace(' ','-')
  page.goto(f'https://www.vpap.org/elections/early-voting/year-2020/{county_url}-va')
  
  county_records = []
  
  for n in range(1,100):
  
    selector = f'#timeline g.popovers rect:nth-of-type({n})'
    try:
      date = page.get_attribute(selector, 'data-original-title')
      vals = page.get_attribute(selector, 'data-content')
    except:
      break

    # process data into tabular structure
    vals_method = re.search('In-Person: (\d+)Mail: (\d+)Total: (\d+)', vals.replace(',',''))
    date_parse = datetime.datetime.strptime(date + ' 2020', '%b %d %Y').strftime('%Y-%m-%d')
    county_records.append([county, date_parse, 'In-Person', vals_method.group(1)])
    county_records.append([county, date_parse, 'Mail', vals_method.group(2)])
    
  return county_records