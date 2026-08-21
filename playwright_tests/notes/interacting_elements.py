#Below are notes on interacting with web elements:

'''
🎭 Day 3 — Interacting With Elements
Today's core methods are:
.click()
.fill()
.check()
.uncheck()
.select_option()
We'll also briefly introduce:
.press()
You don't need to memorize every possible Playwright action. The goal is to understand the pattern:
Find element → Perform action
For example:
page.get_by_role("button", name="Login").click()
1. .click()
This is probably the first method you'll use constantly.
Suppose you have:
page.get_by_role("button", name="Login")
That finds the button.
To actually click it:
page.get_by_role("button", name="Login").click()
Think of it as:
get_by_role()
      ↓
Find the element
      ↓
.click()
      ↓
Interact with it
You can also use a CSS locator:
page.locator("#login").click()
2. .fill()
This is how you'll enter text into inputs.
For example:
page.locator("#username").fill("admin")
This means:
Find the username input and enter admin.
Another example:
page.locator("#password").fill("password123")
This is extremely common in login testing.
You could also use a role:
page.get_by_role("textbox").fill("admin")
Although for forms, get_by_label() can often be more descriptive:
page.get_by_label("Username").fill("admin")
3. .check()
For checkboxes:
page.get_by_role("checkbox", name="Remember me").check()
This checks the box.
For example:
☐ Remember me
becomes:
☑ Remember me
You can also use:
page.locator("#remember").check()
4. .uncheck()
As you'd expect:
page.get_by_role("checkbox", name="Remember me").uncheck()
This removes the check.
You don't necessarily need to use .uncheck() very often, but it's good to know it exists.
5. .select_option()
This is used with dropdowns.
Imagine:
Country
[ United States ▼ ]

United States
Canada
Mexico
You might have:
page.locator("#country").select_option("US")
The exact value depends on the HTML.
For example, the HTML might look like:
<select id="country">
    <option value="US">United States</option>
    <option value="CA">Canada</option>
    <option value="MX">Mexico</option>
</select>
Then:
page.locator("#country").select_option("US")
selects United States.
You can also sometimes select based on the visible label:
page.locator("#country").select_option(label="United States")
6. .press()
This one is useful when you want to simulate a keyboard key.
For example:
page.locator("#search").press("Enter")
This means:
Find the search box and press Enter.
You might use:
page.locator("#search").fill("Playwright")
page.locator("#search").press("Enter")
This is a very realistic automation scenario.
The Pattern I Want You To Learn
Notice something important.
You already learned this:
page.get_by_role("button", name="Login")
Today we're adding:
.click()
So now:
page.get_by_role("button", name="Login").click()
The first part answers:
What element?
The second part answers:
What should I do with it?
That's the fundamental Playwright pattern.
'''