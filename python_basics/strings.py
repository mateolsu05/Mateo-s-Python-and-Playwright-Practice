#below is some practice with strings
course = "Python's for beginners"
print(course)
course = 'Python for "Beginners"'
print(course)


course = '''
Hi John,

Here is our first email to you

Thank you,
The Support team

'''
print(course)



course = "Python for beginners"
print(course[0])
print(course[-1])
print(course[0:3])

#Formatted Strings

first = "John"
last = "Smith"
message = first + " [" + last + "] is a coder"

msg = f"{first} [{last}] is a coder"

print(message)
print(msg)

#String Methods
new_course = "Python for beginners"

print(new_course.upper())
print(len(new_course))
print(new_course.lower())
print(new_course)
print(new_course.find("P"))
print(new_course.find("beginners"))
print(new_course.replace("beginners", "absolute beginners"))

print("Python" in new_course)
print("python" in new_course)