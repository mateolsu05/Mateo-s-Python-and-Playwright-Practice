from playwright.sync_api import sync_playwright

def test_playwright_dev():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://playwright.dev")
        browser.close()