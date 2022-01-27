import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto("https://www.hvz.baden-wuerttemberg.de/overview.html")
        print(await page.title())
        # pause to inspect the page
        # await page.pause()
        await browser.close()

asyncio.run(main())