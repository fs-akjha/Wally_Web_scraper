from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    for browser_type in [p.chromium, p.firefox, p.webkit]:
        browser = browser_type.launch(headless=True)
        page = browser.new_page()
        page.goto('https://duckduckgo.com/')
        element = page.query_selector('input[id=\"search_form_input_homepage\"]')
        parent = element.query_selector('xpath=..')
        grandparent = element.query_selector('xpath=../..')
        siblings = element.query_selector_all('xpath=following-sibling::*')
        children = element.query_selector_all('xpath=child::*')
        browser.close()