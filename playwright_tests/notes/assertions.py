#Below are notes on Assertions:
'''
Day 4 — Assertions
So far, your tests have been doing this:
Open → Find → Fill → Click → Done
But there's a problem.
Imagine your login test:
page.locator("#login-button").click()
The test finishes.
But did login actually work?
We don't know.
That's where assertions come in.
1. What is an assertion?
An assertion basically says:
"I expect this to be true."
In Playwright, you'll commonly use:
from playwright.sync_api import expect
Then:
expect(page.locator("h1")).to_have_text("Products")
This means:
"I expect this heading to contain the text Products."
If it does → ✅ Test passes.
If it doesn't → ❌ Test fails.
2. Your SauceDemo Test With an Assertion
You already had:
page.locator("#user-name").fill("standard_user")
page.locator("#password").fill("secret_sauce")
page.locator("#login-button").click()
Now let's add:
expect(page.locator(".title")).to_have_text("Products")
Your test becomes:
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

        browser.close()
Now we're actually testing something.
3. Common Assertions
You don't need to memorize all of these yet.
Text
expect(locator).to_have_text("Products")
Visible
expect(locator).to_be_visible()
Hidden
expect(locator).to_be_hidden()
Enabled
expect(locator).to_be_enabled()
Disabled
expect(locator).to_be_disabled()
Checked
expect(locator).to_be_checked()
URL
You can also verify the page URL:
expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
⭐ The Big Concept
This:
page.locator("#login-button").click()
is an action.
This:
expect(page.locator(".title")).to_have_text("Products")
is a verification.
That's the distinction I want you to remember.
ACTION
   ↓
Something happens
   ↓
ASSERTION
   ↓
Was the result correct?
Day 4 Practice
Modify your SauceDemo test.
After logging in:
Exercise 1
Verify that:
Products
is visible.
Exercise 2
Verify the URL changed to the inventory page.
Exercise 3
Add a product to the cart and verify that the cart contains the expected item.
Challenge
Create a test that:
Opens SauceDemo
Logs in
Verifies the Products page
Adds the Sauce Labs Onesie
Opens the cart
Verifies the Onesie is in the cart
This is your first real end-to-end test.
🎭 Day 5 — Waiting
Now we get into something that will make a lot more sense after Day 4.
You might remember that you've been using:
page.wait_for_timeout(3000)
We talked about how this pauses the test for exactly three seconds.
But there's a problem.
Imagine your website takes:
1 second → loads
You're still waiting 3 seconds.
Or:
5 seconds → loads
Your 3-second wait isn't enough.
That's why fixed waits aren't ideal.
1. Playwright's Automatic Waiting
One of Playwright's biggest advantages is that it automatically waits for elements to be ready before performing actions.
For example:
page.get_by_role("button", name="Login").click()
Playwright doesn't blindly click immediately.
It waits for the button to be in an actionable state.
That's one reason your tests can be fast and reliable.
2. Assertions Also Wait
This is really important.
When you write:
expect(page.locator(".title")).to_have_text("Products")
Playwright doesn't necessarily check once and immediately fail.
It will automatically retry the assertion for a period of time while waiting for the expected condition.
So if the page needs a moment to update:
Click Login
     ↓
Page begins loading
     ↓
Products appears
     ↓
Assertion sees Products
     ↓
PASS
You don't need:
page.wait_for_timeout(3000)
between every step.
3. Why This Matters
Consider this:
page.click("#login")
page.wait_for_timeout(3000)
expect(page.locator(".title")).to_have_text("Products")
versus:
page.click("#login")
expect(page.locator(".title")).to_have_text("Products")
The second version is generally better.
Why?
Because you're saying:
"I don't care exactly how long this takes. I care that the expected condition eventually happens."
That's a much better testing philosophy.
4. Explicit Waiting
Sometimes you do need to wait for something specific.
For example:
page.wait_for_selector("#something")
or:
page.wait_for_url("**/dashboard")
But don't immediately reach for explicit waits.
First ask:
"Does Playwright already wait for this automatically?"
Very often, the answer is yes.
5. What About time.sleep()?
You may eventually see:
import time

time.sleep(3)
Don't use that as your normal Playwright waiting strategy either.
It's basically:
"Stop everything for three seconds."
Playwright's waiting mechanisms are much more intelligent.
🧠 Your Day 4 + 5 Mental Model
You've now got:
DAY 1
Open browser
     ↓
DAY 2
Find element
     ↓
DAY 3
Interact
     ↓
DAY 4
Verify result
     ↓
DAY 5
Wait intelligently
Which gives us the complete basic test workflow:
       OPEN
         ↓
       FIND
         ↓
      INTERACT
         ↓
       WAIT
         ↓
      ASSERT
         ↓
       PASS/FAIL
And that's real Playwright testing.
'''