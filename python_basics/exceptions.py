#These are notes for exception handling:
#Exception = error that occurs while program is running
'''
For example:
number = int(input("Enter a number: "))
If the user enters:
42
Everything works.
But if they enter:
hello
Python doesn't know how to convert "hello" into an integer, so it crashes with something like:
ValueError: invalid literal for int()
Without exception handling, the program stops immediately.


Using try and except
Instead of letting the program crash, you can catch the error.
try:
    number = int(input("Enter a number: "))
    print(f"You entered {number}")
except ValueError:
    print("Please enter a valid number.")
Now if the user types:
hello
Output:
Please enter a valid number.
The program doesn't crash.

Catching Different Errors
Different mistakes produce different exceptions.
Example:
numbers = [10, 20, 30]

try:
    print(numbers[5])
except IndexError:
    print("That index doesn't exist.")
Output:
That index doesn't exist.

Multiple Exceptions
You can catch different errors separately.
try:
    number = int(input("Enter a number: "))
    print(numbers[number])

except ValueError:
    print("That's not a number.")

except IndexError:
    print("Index out of range.")

else
else runs only if no exception occurred.
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid input.")
else:
    print("Everything worked!")


finally
finally always runs.
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid.")
finally:
    print("Program finished.")
Whether an exception happens or not:
Program finished.
always prints.

'''

