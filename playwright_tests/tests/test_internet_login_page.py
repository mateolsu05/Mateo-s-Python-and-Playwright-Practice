from playwright.sync_api import sync_playwright, expect
from pages.the_internet.login_page import LoginPage



def test_login_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/login")

        login_page = LoginPage(page)
        login_page.login("tomsmith", "SuperSecretPassword!")

        expect(page.locator(".subheader")).to_have_text("Welcome to the Secure Area. When you are done click logout below.")
        #Could do .to_contain_text

        browser.close()