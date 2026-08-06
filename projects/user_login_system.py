#This is a project to simulate a user login system

users = [
    {
        "username": "admin",
        "password": "1234",
        "role": "Administrator",
        "active": True
    },
    {
        "username": "tester",
        "password": "5678",
        "role": "Tester",
        "active": False
    },
    {
        "username": "manager",
        "password": "9999",
        "role": "Manager",
        "active": True
    }
]

def find_user(username):
    for user in users:
        if user["username"] == username:
            return user

    return None

def can_login(user):
    if user["active"]:
        return True
    else:
        return False

def login(username, password):
    actual_username = find_user(username)
    if actual_username and actual_username["password"] == password and actual_username["active"]:
        print("Login successful!")
    elif actual_username and actual_username["password"] != password:
        print("Incorrect password.")
    elif not actual_username:
        print("User not found.")
    elif actual_username and actual_username["password"] == password and not actual_username["active"]:
        print("Account is inactive.")



Username = input("Please enter your username: ")
Password = input("Please enter your password: ")

login(Username, Password)












