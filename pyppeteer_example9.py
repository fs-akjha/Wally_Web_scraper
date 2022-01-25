import asyncio
from pyppeteer import launch

async def intercept_network_request(request):
    # Print some info about the request
    print("URL:", request.url)
    print("Method:", request.method)
    print("Headers:", request.headers)
    # NOTE: You can also await request.abort() to abort the requst1
    await request.continue_()

async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.setRequestInterception(True)
    
    page.on('request', intercept_network_request)
            
    await page.goto('https://techoverflow.net')
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())