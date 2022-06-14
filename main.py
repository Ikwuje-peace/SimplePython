#This short python code is a guessing game.
import random
number = random.randint(1, 20)
guess = int(input("Please enter a number from 1 - 20 "))
while guess != number:
    #This code checks if the users guess is less than the actual number that the computer picked at random
    # If this is true then it urges the user to guess higher
    if guess < number:
        print("Guess Higher")

        # This code checks to see if the user guesses something that is
        # higher than the random number the computer picked
        # and urges the user to guess lower
    else:
        print("Guess lower")
    guess = int(input())
    if guess == number:
        print("YOu got it correctly this time")
    print("You got it correctly this time")
