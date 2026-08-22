#Below are notes on a POM:
'''
Day 6 — Page Object Model
So far, you've been writing tests like this:
def test_login():
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()
That works perfectly fine for learning.
But imagine you have 20 tests that need to log in.
You might end up repeating:
page.locator("#user-name").fill(...)
page.locator("#password").fill(...)
page.locator("#login-button").click()
over and over.
That's where Page Object Model comes in.
1. What is Page Object Model?
The basic idea is:
Put the elements and actions associated with a page into a class.
Instead of your test knowing how to log in, your test simply says:
login_page.login("standard_user", "secret_sauce")
The LoginPage class handles the details.
Think of it like:
Test
 ↓
"Log in"
 ↓
LoginPage
 ↓
username field
password field
login button
Your test becomes cleaner.
2. Creating Your First Page Class
Let's create a file:
pages/login_page.py
Inside:
class LoginPage:

    def __init__(self, page):
        self.page = page
This is where your Python knowledge comes back.
Remember classes?
class Dog:
and:
def __init__(self):
Same concept.
We're creating a Python object that represents the Login Page.
3. Store Your Locators
Now we can put the SauceDemo locators inside the class:
class LoginPage:

    def __init__(self, page):
        self.page = page

        self.username = page.locator("#user-name")
        self.password = page.locator("#password")
        self.login_button = page.locator("#login-button")
Now we've created three attributes:
self.username
self.password
self.login_button
They represent elements on the page.
4. Create a Login Method
Now we can create a function inside the class:
class LoginPage:

    def __init__(self, page):
        self.page = page

        self.username = page.locator("#user-name")
        self.password = page.locator("#password")
        self.login_button = page.locator("#login-button")

    def login(self, username, password):
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()
Look at what we've done.
Instead of having this in our test:
page.locator("#user-name").fill("standard_user")
page.locator("#password").fill("secret_sauce")
page.locator("#login-button").click()
we can now simply write:
login_page.login("standard_user", "secret_sauce")
That's the power of POM.
5. Using the Page Object in a Test
Now your test can look like:
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage


def test_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.saucedemo.com/")

        login_page = LoginPage(page)

        login_page.login("standard_user", "secret_sauce")

        browser.close()
Notice something important:
Your test doesn't know the locators anymore.
It doesn't know:
#user-name
#password
#login-button
It just knows:
login_page.login(...)
That's exactly what we want.
🧠 Why is this useful?
Imagine SauceDemo changes:
id="login-button"
to:
id="submit-login"
Without POM, you'd potentially need to search through many test files.
With POM, you change:
self.login_button = page.locator("#login-button")
to:
self.login_button = page.locator("#submit-login")
And all tests using:
login_page.login(...)
benefit from the change.
That's maintainability.
6. Page Objects Don't Have to Represent an Entire Website
This is important.
You don't necessarily create one giant:
class Website:
Instead, you might have:
pages/
│
├── login_page.py
├── inventory_page.py
├── cart_page.py
└── checkout_page.py
Each class handles its own page/functionality.
For SauceDemo, for example:
LoginPage
    ↓
login()

InventoryPage
    ↓
sort_products()
add_product()

CartPage
    ↓
remove_product()
checkout()
This keeps things organized.
7. Let's Build an Inventory Page
Now let's create:
pages/inventory_page.py
Start with:
class InventoryPage:

    def __init__(self, page):
        self.page = page
Then let's add the sorting dropdown:
class InventoryPage:

    def __init__(self, page):
        self.page = page

        self.sort_dropdown = page.get_by_role("combobox")
And a method:
def sort_low_to_high(self):
    self.sort_dropdown.select_option("lohi")
Now you can simply do:
inventory_page.sort_low_to_high()
Again, the test doesn't need to know "lohi".
8. Add the Onesie
We can also create:
self.onesie_button = page.locator(
    "#add-to-cart-sauce-labs-onesie"
)
Then:
def add_onesie(self):
    self.onesie_button.click()
Now your test can say:
inventory_page.add_onesie()
That's much easier to read.
9. Your Test Starts Looking Like a Test Case
Now imagine:
def test_buy_onesie():
    ...

    login_page.login("standard_user", "secret_sauce")

    inventory_page.sort_low_to_high()

    inventory_page.add_onesie()

    cart_page.open_cart()

    ...
Read that as plain English:
Log in → sort products → add Onesie → open cart.
That's what we're after.
The test describes what we're testing.
The Page Objects describe how to interact with the application.
⭐ The Most Important POM Concept
Remember this separation:
Test
WHAT am I testing?
login_page.login(...)
inventory_page.add_onesie()
cart_page.open_cart()
Page Object
HOW do I perform that action?
self.username.fill(...)
self.password.fill(...)
self.login_button.click()
That's the entire philosophy of Page Object Model.
'''