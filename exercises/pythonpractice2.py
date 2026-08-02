#These are practice exercises for branches continued
#Exercise 3

users = [
    {"username": "admin", "role": "Administrator", "active": True},
    {"username": "tester", "role": "Tester", "active": False},
    {"username": "manager", "role": "Manager", "active": True},
]

for user in users:
    if user["active"]:
        print(f"{user['username']} can login")
    else:
        print(f"{user['username']} is inactive")

