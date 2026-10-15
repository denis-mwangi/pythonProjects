print("Welcome to denoe's Computer quiz!")

playing = input("Do you want to play? ")
playing = playing.lower()

if playing != "yes":
    quit()

print("Okay! Let's play :)")
score = 0



# QUESTION 1
answer = input("What does CPU stand for? ").lower()
if answer == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

# QUESTION 2
answer = input("What does GPU stand for? ").lower()
if answer == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

# QUESTION 3
answer = input("What does RAM stand for? ").lower()
if answer == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

# QUESTION 4
answer = input("What does PSU stand for? ").lower()
if answer == "power supply unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect")


percent = (score/4)*100

if percent >= 100:
    print("Bravo")
else:
    print("Nice try")

print(f"You've got {percent}%")