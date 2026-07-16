#Program to simulate if its hot, its a hot day drink plenty of water
#Otherwise, if its cold, its a cold day, wear warm clothes
#Otherwise, its a lovely day

is_hot = False
is_cold = False

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")



'''
Practice Problem:
Price of a house is 1 million dollars
If buyer has good credit
they need to put down 10%

otherwise
they need to put down 20%
print the down payment
'''

price = 1000000

has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.20 * price

print(f"Down payment: ${down_payment}")



#Elif example

score = 88

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")



#Nested if statement example:
age = 22
has_id = True

if age >= 21:

    if has_id:
        print("You may enter.")
    else:
        print("Bring your ID.")

else:
    print("You are not old enough to enter.")