#In this game the computer tries to guess a number you had in mind
# And it should be able to get your guess correctly in 10 guesses
# That is if you follow the instructions carefully and correctly

low = 1
high = 1000
print("Please guess a number between the range {0} and {1}".format(low, high))
input("Press Enter to start")
guesses = 1
while low != high:
    print("\tGuessing in the range of {0} to {1}".format(low, high))
    guess = low + ((high - low) // 2)
    high_low = input("My guess is {}, Should I guess higher or lower? "
                     "Enter h or l or c if I am correct "
                     .format(guess)).casefold()
    if high_low == "h":
        #Guess higher, the low end of the range becomes the guess + 1
        low = guess + 1
    elif high_low == "l":
        #Guess lower, the high end of the range becomes guess - 1
        high = guess - 1
    elif high_low == "c":
        print("Yay I got it in {} guesses".format(guesses))
        break
    else:
        print("Follow the right instructions, please enter h, l or c")
    guesses += 1
else:
    print("{} is your number isn't it".format(low))
    print("I got in {} guesses".format(guesses))

