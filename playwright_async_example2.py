import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        for browser_type in [p.chromium]:
            browser = await browser_type.launch(headless=True)
            page = await browser.new_page()
            await page.goto('https://www.fleetstudio.com/')
            all_items =await page.query_selector('div')
            # await page.locator("button").click()
            print(all_items.inner_text())
            # await page.screenshot(path=f'scrapingant-{browser_type.name}.png')
            await browser.close()

asyncio.get_event_loop().run_until_complete(main())