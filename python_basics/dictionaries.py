#This is the basics of Dictionaries


user ={
    "username": "admin",
    "password": "12345",
    "email": "admin@example.com"
    }

print(user["username"])

#Change a value
user["password"] = "newpassword"

#add a value
user["environment"] = "QA"

#remove a value
del user["email"]



#loop through a dictionary
for key in user:
    print(key)

for key, value in user.items():
    print(key, value)