import asyncio
from pyppeteer import launch

async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.goto('https://techoverflow.net')

    # Fill content into the search field
    content = "pypetteer"
    await page.evaluate(f"""() => {{
        document.getElementById('s').value = '{content}';
    }}""")

    # Now click the search button    
    await page.evaluate(f"""() => {{
        document.getElementById('searchsubmit').dispatchEvent(new MouseEvent('click', {{
            bubbles: true,
            cancelable: true,
            view: window
        }}));
    }}""")

    # Wait until search results page has been loaded
    await page.waitForSelector(".archive-title")

    # Now take screenshot and exit
    await page.screenshot({'path': 'screenshot.png'})
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())
