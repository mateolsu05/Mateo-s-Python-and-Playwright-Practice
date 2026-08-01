#Below is a practice problem that practices using a list of dictionaries
'''
Given problem:
Mini Project
Create this data:
users = [
    {
        "username": "admin",
        "password": "1234",
        "role": "Administrator"
    },
    {
        "username": "tester",
        "password": "5678",
        "role": "Tester"
    },
    {
        "username": "manager",
        "password": "9999",
        "role": "Manager"
    }
]
Now write a loop that prints:
Username: admin | Role: Administrator
Username: tester | Role: Tester
Username: manager | Role: Manager
Hint: Use an f-string inside the loop.
'''


users = [
    {
        "username": "admin",
        "password": "1234",
        "role": "Administrator"
    },
    {
        "username": "tester",
        "password": "5678",
        "role": "Tester"
    },
    {
        "username": "manager",
        "password": "9999",
        "role": "Manager"
    }
]

for user in users:
    print(f"Username: {user['username']} | Role: {user['role']}")