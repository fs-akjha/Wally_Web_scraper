import asyncio
import bs4
import pyppeteer

def get_current_time(content):
    soup = bs4.BeautifulSoup(content, features="lxml")
    clock = soup.find(class_="my-city__digitalClock")
    hour_minutes = clock.contents[3].next_element
    seconds = clock.contents[5].next_element
    return hour_minutes + ":" + seconds

async def main():
    browser = await pyppeteer.launch({"headless": True})
    page = await browser.newPage()
    await page.goto("https://www.timeanddate.com/worldclock/")
    for _ in range(30):
        content = await page.content()
        print(get_current_time(content))
        await asyncio.sleep(1)
    await browser.close()

asyncio.run(main())