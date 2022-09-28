"""A number-guessing game."""
import random

#ask user for name
#greet player with name
name = input("What is your name?")
print("Hi,", name)

def guessing_game():
    """Play guessing game"""
    best_score = float('inf')
    game_on = True
    while game_on:
        guess_num = int(input("Guess a number: "))
        nums = random.randint(0, 100)
        number_of_guess = 1

        while guess_num != nums:
            number_of_guess = number_of_guess + 1
            if guess_num > nums:
                    print("Number too high, guess again!")
                    guess_num = int(input("Guess another number: "))
            elif guess_num < nums:
                    print("Number too low, guess again!")
                    guess_num = int(input("Guess another number: "))
        
        # check if new score. check if number_of_guess < best_score. replace if it is
        if number_of_guess < best_score:
            best_score = number_of_guess
        # ask if you want to play again. if no then set game_on to false
        play_again = input("Do you want to play again? (Y/N)")
        if play_again.upper() == "N":
            # print current high score
            print("Your best score is", best_score)
            return

guessing_game()



#prompt user to guess a number
#cycle through until user guesses the right number
#end when user guesses the number
