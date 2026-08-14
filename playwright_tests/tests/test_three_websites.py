from playwright.sync_api import sync_playwright

def test_three_websites():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://google.com")
        page.goto("https://www.python.org")
        page.goto("https://yahoo.com")
        browser.close()