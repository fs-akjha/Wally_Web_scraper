from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto('http://whatsmyuseragent.org/')
    html_content=page.inner_html("*")
    print(html_content)
    browser.close()