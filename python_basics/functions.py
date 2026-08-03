#Today I start learning about functions, practice below


def say_hello():
    print("Hello")

say_hello()

#Example with parameters
def greet(name):
    print(f"Hello {name}")

greet("Mateo")

#Example with multiple parameters
def login(Username, Password):
    print(f"Logging in as {Username}")
    print(f"Password: {Password}")

login("admin", "1234")


#Example with return values
def add(a, b):
    return a + b

result = add(1, 2)
print(result)

#Example with string concatenation
def create_username(first, last):
    return first + last

username = create_username("Mateo", "Salinas")
print(username)


'''
Local Variables
Variables created inside a function stay inside that function.
def login():
    username = "admin"
    print(username)
Works:
login()
But this fails:
print(username)
Why?
Because username only exists while the function is running.
This is called local scope.
'''

'''
Global Variables
username = "admin"

def show_user():
    print(username)

show_user()
This works because the function can read variables defined outside of it.
However, as a general rule:
Prefer passing data into functions through parameters instead of relying on global variables.
It's easier to understand and test.
'''


#Example with returning booleans
def is_admin(role):
    return role == "Administrator"

print(is_admin("Administrator"))

'''
Another example:
if is_admin(user["role"]):
    print("Full access")
This reads almost like English.
'''



#Below is an example of functions and loops working together:
def greeting(name):
    print(f"Hello {name}")

users = ["John", "Alice", "Bob"]

for user in users:
    greeting(user)

#Below is an example of functions with dictionaries:
def print_user(user):
    print(f"Username: {user['username']}")
    print(f"Role: {user['role']}")

user = {"username": "admin", "role": "Administrator"}

print_user(user)