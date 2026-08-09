#This is the start of classes
#Act as a blueprint


class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role

#Create an object: User is blueprint, admin is object created from user
admin = User("admin", "Administrator")
print(admin.username)
print(admin.role)

'''
What is self?
This confuses almost everyone at first.
Imagine:
admin = User("admin", "Administrator")
Inside Python, self refers to this particular object.
So:
self.username = username
means:
"Store the username inside this object."
Every object gets its own values.
Example:
admin = User("admin", "Administrator")
tester = User("tester", "Tester")
Now:
admin.username
is:
admin
while:
tester.username
is:
tester
Each object keeps track of its own data.
'''


#Methods = Functions inside a class
class Users:
    def __init__(self,username):
        self.username = username

    def greet(self):
        print(f"Hello {self.username}")

admin = Users("admin")
admin.greet()

#Can use for multiple objects

tester = Users("tester")
tester.greet()