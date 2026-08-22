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


'''
Now let's clear up CSS vs HTML
This is a really good question, because I think the terminology is getting mixed together.
There aren't really "CSS locators vs HTML locators" as two completely separate Playwright systems.
Think about it this way:
HTML
HTML creates the elements:
<input id="username" type="text">
<button id="login-button">Login</button>
<input type="checkbox">
CSS is one way of selecting those HTML elements.
1. CSS selectors
If you see:
<input id="username">
You can use the CSS ID selector:
page.locator("#username")
The # means:
Find the element with this ID.
If you see:
<button class="login-button">Login</button>
You can use:
page.locator(".login-button")
The . means:
Find an element with this class.
If you see:
<button id="submit" class="primary">Submit</button>
You could use:
page.locator("#submit")
or:
page.locator(".primary")
or:
page.locator("button")
These are all CSS selectors being passed into:
page.locator()
2. get_by_role()
This is different.
Suppose the HTML is:
<button>Login</button>
You can tell Playwright:
page.get_by_role("button", name="Login")
You're essentially saying:
Find the element whose accessible role is "button" and whose accessible name is "Login."
This is why you liked get_by_role() earlier.
It's often very readable.
For example:
page.get_by_role("button", name="Login")
is immediately understandable.
3. get_by_text()
If the page contains:
<h2>Welcome to the Secure Area</h2>
you could use:
page.get_by_text("Welcome to the Secure Area")
You're saying:
Find the element containing this text.
4. get_by_label()
This is particularly useful for forms.
Suppose you have:
<label for="username">Username</label>
<input id="username">
You can use:
page.get_by_label("Username")
That's excellent for form fields.
5. get_by_placeholder()
If you have:
<input placeholder="Enter your username">
you can use:
page.get_by_placeholder("Enter your username")
So which should you use?
Here's the hierarchy I'd recommend you keep in your head:
Situation	Try this
Element has a good accessible role/name	get_by_role() ⭐
Form field has a label	get_by_label() ⭐
Element has a unique ID	locator("#id") ⭐
Useful placeholder exists	get_by_placeholder()
Need to locate visible text	get_by_text()
Need a CSS class/attribute	locator(".class")
Complex CSS relationship	locator()
XPath	Use mainly when necessary/readability requires it
My recommendation for you
Since you've told me that page.locator() feels natural to you, keep using it.
You don't need to force yourself to use get_by_role() everywhere.
I would actually like you to become comfortable with both:
page.locator("#username")
and:
page.get_by_role("textbox", name="Username")
Then you can look at a page and decide which makes the most sense.
And here's the big rule
Don't think:
"Which locator am I supposed to memorize?"
Think:
"What information does the HTML give me that uniquely identifies this element?"
For example:
<input id="username">
You immediately have:
page.locator("#username")
If you have:
<button>Login</button>
you might use:
page.get_by_role("button", name="Login")
If you have:
<label>Username</label>
<input>
you might use:
page.get_by_label("Username")
You're reading the page and choosing the locator, rather than blindly trying different methods.
And this checkbox exercise was actually useful
You initially tried:
page.get_by_role("#checkboxes", ...)
The mistake wasn't that you didn't understand checkboxes.
You actually understood the HTML element you wanted.
The mistake was simply that you thought the first argument to get_by_role() was a selector.
Now you know:
get_by_role("checkbox")
             ↑
          ROLE
while:
locator("#checkboxes")
         ↑
      CSS selector
That's an important distinction.
And honestly, this is exactly the kind of mistake I want you making during practice rather than your first week on the job. You're encountering the locator problem, figuring out why it doesn't work, and now you understand the distinction.
You're progressing nicely through this mini-project. Next up is the dropdown, which should be much easier given what you already learned with SauceDemo.
'''