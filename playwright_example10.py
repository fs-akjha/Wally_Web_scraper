from playwright.sync_api import sync_playwright

def main():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=True)
        page=browser.new_page()
        page.goto('https://unsplash.com/')
        page.wait_for_timeout(5000)
        heading_title_selector='*'
        heading=page.query_selector(heading_title_selector)
        print(heading.inner_html())
        browser.close()


if __name__=='__main__':
    main()