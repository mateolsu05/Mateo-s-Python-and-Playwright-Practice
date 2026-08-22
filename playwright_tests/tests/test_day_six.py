from playwright.sync_api import sync_playwright, expect
from pages.sauce_demo.login_page import LoginPage
from pages.sauce_demo.inventory_page import InventoryPage

def test_day_six():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com")

        login_page = LoginPage(page)


        login_page.login("standard_user", "secret_sauce")
        expect(page.locator(".title")).to_have_text("Products")

        inventory_page = InventoryPage(page)
        inventory_page.sort_low_to_high()
        inventory_page.add_onesie()


        browser.close()