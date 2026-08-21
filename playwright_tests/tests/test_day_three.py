#This is a playwright challenge from day 3:
#This test will do the following:
#1. Go to the SauceDemo website.
#2. Log in with the standard_user credentials.
#3. Sort the products from low to high.
#4. Add the Sauce Labs Bike Light to the cart.
from playwright.sync_api import sync_playwright

def test_day_three():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com")
        page.locator("#user-name").fill("standard_user")
        page.locator("#password").fill("secret_sauce")
        page.locator("#login-button").click()
        page.get_by_role("combobox").select_option("lohi")
        page.locator("#add-to-cart-sauce-labs-bike-light").click()
        browser.close()