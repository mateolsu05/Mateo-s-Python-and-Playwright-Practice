#Below is some practice regarding type conversion

birth_year = input("Birth year: ")
print(type(birth_year))
age = 2026 - int(birth_year)
print(age)


#Practice problem from coding with mosh
#Ask a user their weight in pounds, convert to kg, print terminal

user_weight = input("How much do you weigh? ")
weight_in_kg = float(user_weight) * 0.45
print(weight_in_kg)