#Below is my challenge code for Day 4 — Assertions:
#This test will do the following:
#1. Go to the SauceDemo website. Done
#2. Log in with the standard_user credentials. Done
#3. Verify that the Products title is visible. Done
#4. Adds the Sauce Labs Onsie to the cart. Done
#5. Verifies the onsie is the cart. Done

from playwright.sync_api import sync_playwright, expect

def test_day_four():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com")
        page.locator("#user-name").fill("standard_user")
        page.locator("#password").fill("secret_sauce")
        page.locator("#login-button").click()
        expect(page.locator(".title")).to_have_text("Products")
        page.locator("#add-to-cart-sauce-labs-onesie").click()
        page.locator(".shopping_cart_link").click()
        expect(page.locator(".inventory_item_name")).to_have_text("Sauce Labs Onesie")

        browser.close()
