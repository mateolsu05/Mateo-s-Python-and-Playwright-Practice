#These are practice exercises for loops
'''
Notes:3. enumerate() allows you to track indexes in loop

users = ["admin", "tester", "manager"]

for index, user in enumerate(users):
    print(index, user)
Output:
0 admin
1 tester
2 manager

If you want numbering to start at 1:
for index, user in enumerate(users, start=1):
    print(f"{index}. {user}")
Output:
1. admin
2. tester
3. manager
This is exactly what I hinted at yesterday.
You'll often use enumerate() when reporting test results.


4. Looping Through Dictionaries
Suppose:
user = {
    "username": "admin",
    "role": "Administrator",
    "active": True
}
Keys
for key in user:
    print(key)
Output:
username
role
active
Values
for value in user.values():
    print(value)
Output:
admin
Administrator
True

Keys and Values
This is the one you'll use most.
for key, value in user.items():
    print(f"{key}: {value}")
Output:
username: admin
role: Administrator
active: True


continue
Sometimes you want to skip just one iteration.
for number in range(5):
    if number == 2:
        continue

    print(number)
Output:
0
1
3
4
Python skips printing 2 but continues with the rest of the loop.

break
Sometimes you want to stop looping early.
for number in range(10):
    if number == 5:
        break

    print(number)
Output:
0
1
2
3
4
When Python reaches 5, it exits the loop immediately.
'''




#Exercise 1
users = [
    {"username": "admin", "role": "Administrator"},
    {"username": "tester", "role": "Tester"},
    {"username": "manager", "role": "Manager"}
]


'''
Print:
1. admin - Administrator
2. tester - Tester
3. manager - Manager
Hint: Use enumerate(..., start=1).
'''
for index, user in enumerate(users, start=1):
    print (f"{index}. {user['username']} - {user['role']}")



#Exercise 2:
user = {
    "username": "admin",
    "role": "Administrator",
    "active": True
}

for key, value in user.items():
    print(f"{key}: {value}")



#Challenge
pages = [
    "/",
    "/login",
    "/dashboard",
    "/settings"
]

'''
Print:
Checking /
Checking /login
Checking /settings
Skip /dashboard.
Try to solve it using continue.
'''
for page in pages:
    if page == "/dashboard":
        continue
    print(f"Checking {page}")



#More function practice (Calculator):

def add (a, b):
    return a + b

def subtract (a, b):
    return a - b

def multiply (a, b):
    return a * b

def divide (a, b):
    return a / b

def power (a, b):
    return a ** b

print(add(1,2))
print(subtract(1,2))
print(multiply(1,2))
print(divide(1,2))
print(power(1,2))


#Grade Calculator function

def grade_calc(grade):
    if grade >= 90:
        grade = "A"
        return grade
    elif grade >= 80:
        grade = "B"
        return grade
    elif grade >= 70:
        grade = "C"
        return grade
    elif grade >= 60:
        grade = "D"
        return grade
    else:
        grade = "F"
        return grade

print(grade_calc(95))
print(grade_calc(85))
print(grade_calc(75))
print(grade_calc(65))
print(grade_calc(55))


#Function to add money

def add_display_money(a, b):
    c = a + b
    print(c)


add_display_money(95, 65)