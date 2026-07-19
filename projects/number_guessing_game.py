'''
Week 2 Challenge: Number Guessing Game
Create a program that:
Sets a secret number (for example, 7).
Repeatedly asks the user to guess the number.
If the guess is too low, print "Too low!".
If the guess is too high, print "Too high!".
If the guess is correct, print "You got it!" and end the loop using break.
Bonus challenges:
Count how many guesses the user needed.
Let the user type "quit" to exit the game early.
After they win, tell them whether they solved it in 1 guess, 2–5 guesses, or more than 5 guesses using if/elif/else.

'''

secret_number = 7
guess_count = 0
user_guess = int(input("Enter your guess: "))

while user_guess != secret_number:
    if user_guess < secret_number:
        print("Too low!")
        guess_count += 1
        user_guess = int(input("Enter your guess: "))
    elif user_guess > secret_number:
        print("Too high!")
        guess_count += 1
        user_guess = int(input("Enter your guess: "))
    elif user_guess == secret_number:
        print("You got it!")
        guess_count += 1
        break
print("You got it!")
print(f"You guessed {guess_count} times to get it correctly!")

