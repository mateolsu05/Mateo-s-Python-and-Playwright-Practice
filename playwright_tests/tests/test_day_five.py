#Below is the code for the day 5 challenge:
#This test will do the following:
#1. Go to the SauceDemo website. Done
#2. Log in with the standard_user credentials. Done
#3. Verify Products title is visible. Done
#4 Add the sauce labs onesie Done
#5. Navigate to shopping cart Done
#6. Assert that Onesie is in cart Done
#7. Don't use any wait times

from playwright.sync_api import sync_playwright, expect

def test_day_five():
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