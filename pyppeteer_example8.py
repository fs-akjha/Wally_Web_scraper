import asyncio
from pyppeteer import launch
async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.goto('https://techoverflow.net')
    
    # This example fills content into the search field
    content = "My search term"
    await page.evaluate(f"""() => {{
        document.getElementById('s').value = '{content}';
    }}""")
    # Make screenshot
    await page.screenshot({'path': 'screenshot.png'})
    await browser.close()
asyncio.get_event_loop().run_until_complete(main())