from playwright.sync_api import sync_playwright, expect
from pages.the_internet.checkbox_page import CheckboxPage

def test_checkbox_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/checkboxes")

        checkbox_page = CheckboxPage(page)
        checkbox_page.check_first_check_box()
        checkbox_page.uncheck_second_check_box()

        expect(page.get_by_role("checkbox").nth(0)).to_be_checked()
        expect(page.get_by_role("checkbox").nth(1)).not_to_be_checked()
        #Use for future reference:
        #expect(checkbox_page.checkbox_one).to_be_checked()
        #expect(checkbox_page.checkbox_two).not_to_be_checked()

        browser.close()