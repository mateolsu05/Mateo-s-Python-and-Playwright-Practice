from playwright.sync_api import sync_playwright

def test_two_tabs():
   with sync_playwright() as p:
       browser = p.chromium.launch(headless=False)
       page1 = browser.new_page()
       page1.goto("https://yahoo.com")
       page2 = browser.new_page()
       page2.goto("https://google.com")
       browser.close()
