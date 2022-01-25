from turtle import heading
from playwright.sync_api import sync_playwright


def main():
    with sync_playwright() as p:
        browser=p.webkit.launch(headless=True)    #It will launch the chromium in headless mode and perform the operation accordingly, by default the playwright is headless.
        page=browser.new_page()                     #It will return the instance of the page
        page.goto('https://quotes.toscrape.com/')
        quotes=page.query_selector_all('[class="quote"]')
        for quote in quotes:
            print(quote.query_selector('.text').inner_text())
        page.wait_for_timeout(2000)                 #Instead of using sleep need to use wait_for_timeout()
        browser.close()                             #To Closr the launched Browser



if __name__=='__main__':
    main()