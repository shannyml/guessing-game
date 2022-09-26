"""A number-guessing game."""
import random

#ask user for name
#greet player with name
name = input("What is your name?")
print("Hi,", name)
guess_num_input = input("Guess a number: ")
guess_num = int(guess_num_input)

nums = random.randint(0, 100)

while guess_num != nums:

    if guess_num > nums:
        print("Number too high, guess again!")
        guess_num = int(input("Guess another number: "))
    elif guess_num < nums:
        print("Number too low, guess again!")
        guess_num = int(input("Guess another number: "))
print("You did it! The number is", nums)
#prompt user to guess a number
#cycle through until user guesses the right number
#end when user guesses the number
