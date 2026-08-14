#This is my first test with Playwright!:

from playwright.sync_api import sync_playwright

def test_open_google():
    with sync_playwright() as p:        #Starts Playwright Engine
        browser = p.chromium.launch(headless=False)     #Use P, then chromium is selected browser, launch = launches browser, headless = false means actually see browser window
        page = browser.new_page()   #technically like launching a new tab in browser
        page.goto("https://www.google.com")
        browser.close()

#Understanding Flow of a Playwright test:
#Start Playwright -> Launch Browser -> Open Tab -> Go to Website -> Close Browser