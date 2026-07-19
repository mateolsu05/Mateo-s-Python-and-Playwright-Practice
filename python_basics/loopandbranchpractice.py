#Exercise 1: write program that prints:
#"Adult" if age is 18 or older.
#"Minor" otherwise.

age = 16

if age >= 18:
    print("Adult")
else:
    print("Minor")


'''
Exercise 2
Given:
users = ["Alice", "Bob", "Charlie", "David"]
Use a for loop to print:
Welcome Alice
Welcome Bob
Welcome Charlie
Welcome David
'''

users = ["Alice", "Bob", "Charlie", "David"]

for user in users:
    print(f"Welcome {user}")



'''
Use a while loop to count from 10 down to 1, then print:
Blast off!
'''

count = 10
while count > 0:
    print(count)
    count = count - 1
print("Blast off!")



'''
Exercise 4 (Automation Style)
You have a list of login results:
results = [True, True, False, True]
Loop through them and print:
"PASS" for True
"FAIL" for False
'''
results = [True, True, False, True]
for result in results:
    if result == True:
        print("PASS")
    else:
        print("FAIL")