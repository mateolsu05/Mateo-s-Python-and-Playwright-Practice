from playwright.sync_api import sync_playwright, expect
from pages.sauce_demo.login_page import LoginPage

def test_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.saucedemo.com")

        login_page = LoginPage(page)

        login_page.login("standard_user", "secret_sauce")

        expect(page.locator(".title")).to_have_text("Products")

        browser.close()