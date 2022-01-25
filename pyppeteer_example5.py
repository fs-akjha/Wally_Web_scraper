import asyncio
from pyppeteer import launch
async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.goto('https://www.techoverflow.net')
    # Get the URL and print it
    title = await page.evaluate("() => document.querySelector('.logo-default').textContent")
    print(f"Page title: {title}") # prints Page title: TechOverflow
    # Cleanup
    await browser.close()
asyncio.get_event_loop().run_until_complete(main())