#Introduction to lists:
users = ["Alice", "Bob", "Charlie", "David"]
print(users)
print(users[0])
print(users[1])
print(users[2])

#Negative Indexes = just backwards
print(users[-1])
print(users[-2])

#Changing Items in a list:
#Replaces index one with Steven
users[1] = "Steven"
print(users)

#Adding Items in a list:
#use append
users.append("John")
print(users)

#Removing Items in a list:
#use remove
users.remove("John")
print(users)

#pop by index
users.pop(1)
print(users)


#Find Length
print(len(users))


#Check if something is in list
if "Alice" in users:
    print("User found")

#Looping through a list
for user in users:
    print(user)


#Automation Example

browsers = ["Chrome", "Firefox", "Edge"]
for browser in browsers:
    print(f"Running tests in {browser}")

#Practice exercises:
'''
Exercise 1
Create a list called colors containing:
Red
Blue
Green
Yellow
Print:
The first color
The last color
'''
colors = ["Red", "Blue", "Green", "Yellow"]
print(colors[0])
print(colors[-1])

'''
Exercise 2
Start with:
animals = ["Dog", "Cat"]
Add:
Bird
Fish
Print the finished list.
'''
animals = ["Dog", "Cat"]
animals.append("Bird")
animals.append("Fish")
print(animals)


'''
Exercise 3
Start with:
numbers = [10, 20, 30, 40]
Change 20 to 25.
Print the updated list.
'''
numbers = [10, 20, 30, 40]
numbers[1] = 25
print(numbers)


'''
Exercise 4
Given:
frameworks = ["Playwright", "Selenium", "Cypress"]
Write code that prints:
Learning Playwright
Learning Selenium
Learning Cypress
using a for loop.
'''
frameworks = ["Playwright", "Selenium", "Cypress"]
for framework in frameworks:
    print(f"Learning {framework}")


#Challenge Exercise:
'''
Challenge Exercise
Start with:
results = ["PASS", "FAIL", "PASS"]
Write code that prints:
There are 3 test results.
Hint: You'll need len().
'''

results = ["PASS", "FAIL", "PASS"]
print(f"There are {len(results)} test results.")