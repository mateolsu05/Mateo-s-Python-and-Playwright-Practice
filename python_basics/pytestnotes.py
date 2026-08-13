#Below are my notes on pytest:
'''
What is pytest?
pytest is a testing framework.
Instead of writing:
print("Login Successful")
you write code that verifies something is true.
For example:
assert 2 + 2 == 4
If it's true:
✅ Test Passed
If it's false:
assert 2 + 2 == 5
pytest says:
❌ Test Failed
Your First Test
Create a file named:
test_math.py
Notice the name starts with:
test_
This is important.
pytest automatically searches for files beginning with:
test_
Inside:
def test_addition():
    assert 2 + 2 == 4
That's it.
Seriously.
Your first automated test.
Running Tests
Open the terminal:
pytest
Output:
==================== test session starts ====================

collected 1 item

test_math.py .                                  [100%]

1 passed
That little dot means:
.
One passing test.
A Failing Test
Now change it.
def test_addition():
    assert 2 + 2 == 5
Run:
pytest
Now you'll see something like:
FAILED test_math.py

E assert 4 == 5
This is one of my favorite things about pytest.
It tells you exactly what was different.
Assertions
Assertions are the heart of testing.
Example:
assert "admin" == "admin"
Passes.
assert len([1,2,3]) == 3
Passes.
assert 10 > 5
Passes.
assert "admin" == "tester"
Fails.
Multiple Tests
def test_addition():
    assert 2 + 2 == 4


def test_subtraction():
    assert 10 - 3 == 7


def test_multiplication():
    assert 5 * 5 == 25
Run:
pytest
Output:
...
3 passed
Each dot represents one passing test.
Testing Your Own Functions
This is where everything comes together.
Remember when you wrote:
def is_even(number):
    return number % 2 == 0
Now you can test it.
def test_even_number():
    assert is_even(4) == True
Another:
def test_odd_number():
    assert is_even(5) == False
Now you're testing your own code.
Testing Classes
Remember your Rectangle class?
class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
Test:
def test_rectangle_area():
    rectangle = Rectangle(5, 10)

    assert rectangle.area() == 50
Now you're testing methods.
Why QA Engineers Love pytest
Imagine a login function.
def login(username, password):
Instead of manually checking:
Username: admin
Password: 1234
You write:
def test_valid_login():
    assert login("admin", "1234") == True
Another:
def test_invalid_password():
    assert login("admin", "wrong") == False
Run:
pytest
Now hundreds of tests can execute in seconds.
Organizing Tests
Eventually your project will look like:
automation_project/

tests/
    test_login.py
    test_dashboard.py
    test_checkout.py

pages/
    login_page.py
    dashboard_page.py

data/
    users.json
Notice:
tests/
This is where your pytest files live
'''