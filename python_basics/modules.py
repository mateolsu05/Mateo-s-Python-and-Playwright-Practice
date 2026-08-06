#Here are notes from modules:
'''
What Does import Do?
Imagine your project looks like this:
project/
│
├── main.py
└── math_tools.py
Inside math_tools.py:
def add(a, b):
    return a + b
Now in main.py:
import math_tools

result = math_tools.add(5, 7)

print(result)
Output:
12
'''


'''
Different Ways to Import
Method 1 (Most Common)
import random
Use it like:
random.randint(1, 10)
Notice the module name comes first.
Method 2
from random import randint
Now you can simply write:
randint(1, 10)
No need for:
random.randint(...)
Which One Should You Use?
For beginners—and in many professional codebases—I recommend:
import random
Why?
Because when you see:
random.randint(...)
it's immediately obvious where randint came from.
Another Example
Python has a module called datetime.
from datetime import datetime
Now:
current_time = datetime.now()

print(current_time)
Very useful in automation for timestamps and logging.
'''

'''
Creating Your Own Module
This is where things get interesting.
Suppose you have:
login.py
def login(username, password):
    print(f"Logging in as {username}")
Then:
main.py
import login

login.login("admin", "1234")
Output:
Logging in as admin
See what's happening?
You're importing your own code, not Python's.
'''