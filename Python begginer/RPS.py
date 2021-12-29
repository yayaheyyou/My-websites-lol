# Modules needed

import random

# The start (Round 1)

print("Welcome to Rock, Paper, Scissors.")

print("Round 1!")

# Variable inputs

userInput = str(input("Input your answer: "))

Rock = "Rock" or "rock"

Paper = "Paper" or "paper"

Scissors = "Scissors" or "scissors"

Choices = [Rock, Paper, Scissors]

RANDOM = random.choice(Choices)

RW = 0
RL = 0
RT = 0

# Conditioning

# In case of "Rock"
if (userInput == Rock and RANDOM == Paper):
       RL += 1
       print("You lost!")

elif (userInput == Rock and RANDOM == Rock):
    RT += 1
    print("It's a tie.")

elif (userInput == Rock and RANDOM == Scissors):
    RW += 1
    print("You won!")

# In case of "Paper"

if (userInput == Paper and RANDOM == Rock):
       RW += 1
       print("You won!")

elif (userInput == Paper and RANDOM == Paper):
    RT += 1
    print("It's a tie.")

elif (userInput == Paper and RANDOM == Scissors):
    RL += 1
    print("You lost!")

# In case of "Scissors"

if (userInput == Scissors and RANDOM == Paper):
       RW += 1
       print("You won!")

elif (userInput == Scissors and RANDOM == Rock):
    RL += 1
    print("You lost!")

elif (userInput == Scissors and RANDOM == Scissors):
    RT += 1
    print("It's a tie.")

print("It was " + RANDOM +".")


##################################################################################################

# Round 2!

print("Round 2!")

userInput2 = str(input("Input your answer: "))

RANDOM2 = random.choice(Choices)

# In case of "Rock"
if (userInput2 == Rock and RANDOM2 == Paper):
       RL += 1
       print("You lost!")

elif (userInput2 == Rock and RANDOM2 == Rock):
    RT += 1
    print("It's a tie.")

elif (userInput2 == Rock and RANDOM2 == Scissors):
    RW += 1
    print("You won!")

# In case of "Paper"

if (userInput2 == Paper and RANDOM2 == Rock):
       RW += 1
       print("You won!")

elif (userInput2 == Paper and RANDOM2 == Paper):
    RT += 1
    print("It's a tie.")

elif (userInput2 == Paper and RANDOM2 == Scissors):
    RL += 1
    print("You lost!")

# In case of "Scissors"

if (userInput2 == Scissors and RANDOM2 == Paper):
       RW += 1
       print("You won!")

elif (userInput2 == Scissors and RANDOM2 == Rock):
    RL += 1
    print("You lost!")

elif (userInput2 == Scissors and RANDOM2 == Scissors):
    RT += 1
    print("It's a tie.")

print("It was " + RANDOM +".")
##################################################################################################

# Round 3!

print("Round 3!")

userInput3 = str(input("Input your answer: "))

RANDOM3 = random.choice(Choices)

# In case of "Rock"
if (userInput3 == Rock and RANDOM3 == Paper):
       RL += 1
       print("You lost!")

elif (userInput3 == Rock and RANDOM3 == Rock):
    RT += 1
    print("It's a tie.")

elif (userInput3 == Rock and RANDOM3 == Scissors):
    RW += 1
    print("You won!")

# In case of "Paper"

if (userInput3 == Paper and RANDOM3 == Rock):
       RW += 1
       print("You won!")

elif (userInput3 == Paper and RANDOM3 == Paper):
    RT += 1
    print("It's a tie.")

elif (userInput3 == Paper and RANDOM3 == Scissors):
    RL += 1
    print("You lost!")

# In case of "Scissors"

if (userInput3 == Scissors and RANDOM3 == Paper):
       RW += 1
       print("You won!")

elif (userInput3 == Scissors and RANDOM3 == Rock):
    RL += 1
    print("You lost!")

elif (userInput3 == Scissors and RANDOM3 == Scissors):
    RT += 1
    print("It's a tie.")

print("It was " + RANDOM +".")


# The end. 

print("You got:- ")
print(str(RW) + " Rounds won!")
print(str(RT) + " Rounds tied.")
print(str(RL) + " Rounds lost!")
