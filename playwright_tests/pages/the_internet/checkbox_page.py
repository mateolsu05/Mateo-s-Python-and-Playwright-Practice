#Goal: Identify two checkboxes, determine initial states, create methods to check, uncheck, use asertions to verify

class CheckboxPage:
    def __init__(self, page):
        self.page = page
        self.checkbox_one = page.get_by_role("checkbox").nth(0)
        self.checkbox_two = page.get_by_role("checkbox").nth(1)

    def check_first_check_box(self):
        self.checkbox_one.check()

    def uncheck_first_check_box(self):
        self.checkbox_one.uncheck()

    def check_second_check_box(self):
        self.checkbox_two.check()

    def uncheck_second_check_box(self):
        self.checkbox_two.uncheck()