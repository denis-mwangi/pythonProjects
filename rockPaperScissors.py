import random

userWins = 0
compWins = 0

options = ['rock','paper','scissors']

while True:
    userInput = input("Type Rock/Paper/Scissors or q to quit. ").lower()
    if userInput == "q":
        break
    if userInput not in options:
        continue
    randomNumber = random.randint(0,2)
    # rock: 0, paper: 1, scissors: 2
    compPick = options[randomNumber]
    print(f"Computer picked {compPick}.")
    
    if userInput == "rock" and compPick == "scissors":
        print("You won")
        userWins += 1
    elif userInput == "paper" and compPick == "rock":
        print("You won")
        userWins += 1
    elif userInput == "scissors" and compPick == "paper":
        print("You won")
        userWins += 1
    else:
        print("You lost!")
        compWins += 1

if userWins > compWins:
    print("You are the winner")
elif userWins == compWins:
    print("It is a stale mate")
else:
    print("Computer wins")      
print(f"You won {userWins} times.")
print(f"Computer won {compWins} times.")