
class InventoryPage:
    def __init__(self, page):
        self.page = page

        self.sort_dropdown = page.get_by_role("combobox")
        self.onesie_button = page.locator("#add-to-cart-sauce-labs-onesie")

    def sort_low_to_high(self):
        self.sort_dropdown.select_option("lohi")

    def add_onesie(self):
        self.onesie_button.click()