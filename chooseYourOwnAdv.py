name = input("Type Your name: ")
print(f"Welcome {name} to this adventure game hope you enjoy.")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way do you go? Type l to go left or r to go right ").lower()

if answer == "l":
    answer = input("You have come to a river, you can walk around it or swim across? Type w to walk around or s to swim across. ").lower()
    if answer == "w":
        print("You walked for many miles, ran out of water and lost the game")
    elif answer == "s":
        print("You tried to swim across but you were eaten by a crocodile.")
    else:
         print("Not a valid input. You lose!")
elif answer == "r":
    answer == input("You come to a bridge, it looks wobbly, do you want to cross it or head back? (c or b) ").lower()
    
    if answer == "c":
        answer = input("You cross the bridge and meet a stranger, do you talk to him or drive past her? (y or n)").lower()
        if answer == "y":
            print("You talk to the girl and she is a princess and she gives you gold")
        elif answer == "n":
            print("You ignore the stranger and later find out she was actually the princess. You lose!")
        else:
            print("Not a valid input. You lose!")
    elif answer == "b":
        print("You go back and lose.")
else:
    print("Not a valid input. You lose!")