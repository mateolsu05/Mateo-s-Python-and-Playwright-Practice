#Below I am testing python.org

from playwright.sync_api import sync_playwright

def test_locator():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.python.org")

    #Find a link:
        page.get_by_role("link", name="Downloads")

    #Find a heading:
        page.get_by_role("heading", name="Welcome to Python.org")

    #Find an element with text:
        page.get_by_text("Python is a programming language that lets you work quickly and integrate systems more effectively.")

    #Find a button:
        page.locator("button")

    #Find a button that has an ID locator:
        page.locator("#submit")

        #Below is find a button using CSS selector:
        #page.locato("button")
        #Below is find a button using XPath:
        #page.locator("//button[@id='submit']")
        browser.close()


        #Big 3 to know: page.get_by_role(), page.get_by_text(), page.locator()