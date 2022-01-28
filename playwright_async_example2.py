import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        for browser_type in [p.chromium]:
            browser = await browser_type.launch(headless=True)
            page = await browser.new_page()
            await page.goto('http://whatsmyuseragent.org/')
            userAgentSelector = "div.user-agent"
            elementHandle = await page.query_selector(userAgentSelector)
            uaHtml = elementHandle.inner_text()
            print("uaHtml=%s" % uaHtml)
            # await page.screenshot(path=f'scrapingant-{browser_type.name}.png')
            await browser.close()

asyncio.get_event_loop().run_until_complete(main())