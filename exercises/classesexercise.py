#These are practice exercises for classes

#Exercise 1:
class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role
    def print(self):
        print(f"{self.username}  {self.role}")
    def greet(self):
        print(f"Welcome {self.username}!")

admin = User("admin", "Administrator")
admin.print()
admin.greet()

tester = User("tester", "Tester")
tester.print()
tester.greet()


#Exercise 2 is above


#Exercise 3:

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

rectangle = Rectangle(5,100)
print(rectangle.area())

#Challenge:

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount
    def show_balance(self):
        print(f"Balance: {self.balance}")

mateoAccount = BankAccount("Mateo", 800)
mateoAccount.deposit(100)
mateoAccount.withdraw(200)
mateoAccount.show_balance()