from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://medium.com/z1digitalstudio/pyppeteer-the-snake-charmer-f3d1843ddb19")
    print(page.title())
    browser.close()