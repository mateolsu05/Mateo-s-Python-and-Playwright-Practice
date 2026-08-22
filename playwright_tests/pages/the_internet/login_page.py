
class LoginPage:
    def __init__(self, page):
        self.page = page

        self.username = page.locator("#username")
        self.password = page.locator("#password")
        self.login_button = page.get_by_role("button", name="Login")

    def login(self, username, password):
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()