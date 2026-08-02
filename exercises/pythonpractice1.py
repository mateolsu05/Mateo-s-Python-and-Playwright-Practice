#These are practice exercises for branches
#Exercise 1
login_data = {
    "username": "admin",
    "password": "1234"
}

entered_username = "admin"
entered_password = "1234"

#write an if statement that prints login successful, otherwise login failed, need and

if login_data["username"] == entered_username and login_data["password"] == entered_password:
    print("Login successful")
else:
    print("Login failed")


#Exercise 2
#loop through list, if role is administrator, print admin has full access
#otherwise tester has limited access
#or manager has limited access
users = [
    {
        "username": "admin",
        "role": "Administrator"
    },
    {
        "username": "tester",
        "role": "Tester"
    },
    {
        "username": "manager",
        "role": "Manager"
    }
]
for user in users:
    if user["role"] == "Administrator":
        print(f"{user['username']} has full access")
    else:
        print(f"{user['username']} has limited access")