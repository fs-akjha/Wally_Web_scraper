from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    for browser_type in [p.chromium]:
        browser = browser_type.launch()
        page = browser.new_page()
        page.goto('http://scrapingant.com/')
        all_items =page.query_selector('h1')
        print(all_items.inner_text())
        # page.screenshot(path=f'scrapingant-{browser_type.name}.png')
        browser.close()