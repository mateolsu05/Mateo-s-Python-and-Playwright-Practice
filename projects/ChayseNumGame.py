#Hello Chayse, here is your number guessing game!

import random


secret_number = random.randint(1, 100)



name = input("Hello! What is your name? ")
print(f"Hello {name}! let us start")

for i in range(6):
    guess = int(input("What is your guess? "))
    if guess == secret_number:
        print(f"You guessed correctly! The number was {secret_number}")
        break
    elif guess > secret_number:
        print(f"You guessed too high!")
    elif guess < secret_number:
        print(f"You guessed too low!")


if secret_number != guess:
    print(f"You lost! The number was {secret_number}")

