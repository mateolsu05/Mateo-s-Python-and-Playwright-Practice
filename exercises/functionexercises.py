#Below is my practice exercises for functions

#Exercise 1
def greet_user(name):
    print(f"Welcome {name}!")

greet_user("John")
greet_user("Alice")
greet_user("Bob")


#Exercise 2
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

print(is_even(4))
print(is_even(7))


#Exercise 3
users = [
    {"username": "admin", "role": "Administrator"},
    {"username": "tester", "role": "Tester"}
]

def print_user(user):
    print(f"Username: {user['username']}")
    print(f"Role: {user['role']}")

for user in users:
    print_user(user)


#Challenge
def can_login(user):
    if user["active"]:
        return True
    else:
        return False

user = {
    "username": "admin",
    "active": True
}

if can_login(user):
    print("Login allowed")
else:
    print("Login denied")
