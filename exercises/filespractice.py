#Below are practice exercises on files:
#Exercise 1:
import json


with open("../data/notes.txt", "w") as file:
    file.write("This is for exercise 1\n")
    file.write("2nd line")

with open("../data/notes.txt", "r") as file:
    contents = file.read()
    print(contents)


#Exercise 2:
user = {
    "username": "admin",
    "role": "Administrator",
    "active": True
}

with open("../data/user.json", "w") as file:
    json.dump(user, file, indent=4)


#Exercise 3:
with open("../data/user.json", "r") as file:
    user = json.load(file)
    print(f"Username: {user['username']}")
    print(f"Role: {user['role']}")


#Challenge:
users = [
    {
        "username": "admin",
        "role": "Administrator"
    },
    {
        "username": "tester",
        "role": "Tester"
    }
]

with open("../data/users.json", "w") as file:
    json.dump(users, file, indent=4)

with open("../data/users.json", "r") as file:
    loaded_users = json.load(file)
    for user in loaded_users:
        print(f"Username: {user['username']}, Role: {user['role']}")