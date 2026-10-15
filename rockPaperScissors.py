import random

userWins = 0
compWins = 0

while True:
    userInput = input("Type Rock/Paper/Scissors or q to quit").lower()
    if userInput == "q":
        quit()
    