import asyncio
from pyppeteer import launch
async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.goto('https://www.techoverflow.net')
    # Get the URL and print it
    url = await page.evaluate("() => window.location.href")
    print(url) # prints https://www.techoverflow.net/
    # Cleanuip
    await browser.close()
asyncio.get_event_loop().run_until_complete(main())