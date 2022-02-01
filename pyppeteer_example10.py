import asyncio
from bs4 import BeautifulSoup
from pyppeteer import launch
import os
from urllib.parse import urljoin, urlparse


async def main():
    # Launch the browser
    browser = await launch()

    # Open a new browser page
    page = await browser.newPage()

    # Create a URI for our test file
    page_path = "https://www.tesla.com"

    # Open our test file in the opened page
    await page.goto(page_path)
    page_content = await page.content()

    # Process extracted content with BeautifulSoup
    soup = BeautifulSoup(page_content)
    quotes=soup.find_all('a')
    print(len(quotes))
    # print(quotes)
    for quo in quotes:
        # print(quo)
        try:
            new_link = urljoin(page_path, quo['href'])
            print(new_link)
        except Exception as e:
                pass
    await browser.close()


asyncio.get_event_loop().run_until_complete(main())