from playwright.sync_api import sync_playwright, expect

def test_sauce():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com/")
        page.locator("#user-name").fill("standard_user")
        page.locator("#password").fill("secret_sauce")
        page.locator("#login-button").click()
        expect(page.locator(".title")).to_have_text("Products")
        expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
        page.get_by_role("combobox").select_option("lohi")
        page.locator("#add-to-cart-sauce-labs-onesie").click()
        page.locator(".shopping_cart_link").click()
        expect(page.locator(".inventory_item_name")).to_have_text("Sauce Labs Onesie")

        page.wait_for_timeout(3000)

        browser.close()