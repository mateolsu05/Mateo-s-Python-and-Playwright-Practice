#Below are practice exercises for exception handling:
#Exercise 1:
try:
    number_given = int(input("Please enter a number: "))
except ValueError:
    print("Please enter a valid number")
else:
    print(f"You entered {number_given}")


#Exercise 2:
numbers = [10, 20, 30]

try:
    number = int(input("Please enter a number: "))
    print(f"Value: {numbers[number]}")
except IndexError:
    print("Index out of range")


#Challenge:
new_numbers = [10, 20, 30]
try:
    new_number = int(input("Please enter a number: "))
    print(f"Value: {new_numbers[new_number]}")
except ValueError:
    print("Please enter a valid number")
except IndexError:
    print("Index out of range")


