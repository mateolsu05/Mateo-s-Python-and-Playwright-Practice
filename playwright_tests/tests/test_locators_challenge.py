from playwright.sync_api import sync_playwright

def test_challenge():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.python.org")

        #The code below gets the Community Link:
        page.get_by_role("link", name="Community")

        #The code below gets the socialize element by looking for text that contains the word "Socialize":
        page.get_by_text("Socialize")

        #The code below should locate the launch interactive shell
        page.locator("#start-shell")

        page.wait_for_timeout(3000)

        browser.close()