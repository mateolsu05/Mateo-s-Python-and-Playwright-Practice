#Below are notes on locators:

'''
What is a Locator?
Imagine you're looking at a webpage:
--------------------------------
        Login
--------------------------------

Username: [____________]

Password: [____________]

        [ Login ]

--------------------------------
If you tell Playwright:
page.locator("#username")
you're essentially saying:
"Find the element on this webpage whose ID is username."
A locator is a way of identifying an element on a webpage.
That element could be:
a button
a textbox
a checkbox
a link
a heading
an image
a dropdown
etc.


Your First Locator
The basic syntax is:
page.locator("selector")
For example:
page.locator("#username")
The # means we're looking for an ID.
Suppose the HTML is:
<input id="username">
Then:
page.locator("#username")
finds that element.


IDs
IDs are one of the easiest selectors to understand.
HTML:
<input id="username">
Playwright:
page.locator("#username")
Another example:
<button id="login">Login</button>
Playwright:
page.locator("#login")
The pattern is:
HTML:
id="something"

Playwright:
#something


CSS Selectors
This is where your existing Python knowledge isn't enough—you'll start learning a little bit of CSS selector syntax.
You don't need to become a CSS expert.
For example:
page.locator("button")
means:
Find a <button> element.
If a page has:
<button>Login</button>
<button>Cancel</button>
then:
page.locator("button")
can identify the buttons.
You can also combine selectors.
For example:
page.locator("input#username")
means:
Find an <input> whose ID is username.


Text
You can also locate elements based on their text.
For example:
page.get_by_text("Login")
If the page contains:
<button>Login</button>
Playwright can find it using:
page.get_by_text("Login")
This is often very readable.


get_by_role() ⭐
This is one of the most important concepts today.
Playwright provides:
page.get_by_role()
This lets you identify elements based on their accessible role.
For example:
page.get_by_role("button")
means:
Find a button.
You can make it more specific:
page.get_by_role("button", name="Login")
That's saying:
Find the button whose accessible name is "Login."
This is generally much more readable than trying to construct complicated CSS selectors.


Common Roles
You don't need to memorize all of these today, but become familiar with them.
Element	Role
Button	"button"
Link	"link"
Heading	"heading"
Checkbox	"checkbox"
Textbox	"textbox"
Radio button	"radio"
Combobox	"combobox"
For example:
page.get_by_role("button", name="Login")
page.get_by_role("link", name="Sign Up")
page.get_by_role("heading", name="Dashboard")
8. Why get_by_role() Is So Useful
Consider these two:
page.locator("#login-button")
and:
page.get_by_role("button", name="Login")
Both can potentially find the same button.
But the second one communicates more clearly what you're looking for:
"Find the Login button."
That's one reason Playwright encourages user-facing locators such as roles, labels, and text when they're appropriate.
9. get_by_label()
Here's another useful locator.
Imagine a form:
<label>Username</label>
<input>
Playwright can sometimes locate the input using:
page.get_by_label("Username")
This is especially useful for forms.
You'll use this more when we get to actual form automation.
10. XPath
You'll probably encounter XPath at work, so you should understand what it looks like.
For example:
page.locator("//button")
or:
page.locator("//input[@id='username']")
You do not need to become an XPath expert.
For our purposes, your goal is:
"I can recognize XPath and understand what it is doing."
For example:
//button
means roughly:
Find a button element.
And:
//input[@id='username']
means:
Find an input whose ID is username.
We'll generally prefer better Playwright locators when they're available.
11. The Locator Hierarchy I Want You to Learn
When you're looking for an element, I want you to start thinking like this:
First choice
page.get_by_role(...)
Then consider
page.get_by_label(...)
or:
page.get_by_text(...)
Then
page.locator(...)
for things such as IDs/CSS selectors.
XPath
Use when necessary, but don't make it your default strategy.
'''