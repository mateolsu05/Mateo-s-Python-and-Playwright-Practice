#For loops
'''
for number in range (5):
    print(number)
'''

for letter in "Python":
    print(letter)



#Range below produces 0-4
range(5)

#Range produces 2-6
range(2,7)

#range produces 0 2 4 6 8 10
range(0,11,2)


#break
for number in range(10):
    if number == 5:
        break

    print(number)


'''
continue:
for number in range(6):
    if number == 5:
        continue
    print(number)

'''