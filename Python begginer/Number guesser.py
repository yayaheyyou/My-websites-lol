# Modules

import random
import math

# The start 

print("Welcome to Guess the number!")
print("In this game you guess numbers based on if they are bigger or smaller.")
print("The numbers range from 1 to 100.")
print("Also you only get 5 chances.")
# Some vars. 

userNumber = int(input("Write your guess: "))

RNG = random.randint(1, 100)

# Conditioning the variables. 

# First chance

if (userNumber > RNG):
    print("It's smaller.")
    userNumber = int(input("Try again: "))
elif (userNumber < RNG):
    print("It's bigger.")
    userNumber = int(input("Try again: "))
elif (userNumber == RNG):
    print("You got it right! Congrats!")

    # Second chance. 

if (userNumber > RNG):
    print("It's smaller.")
    userNumber = int(input("Try again: "))
elif (userNumber < RNG):
    print("It's bigger.")
    userNumber = int(input("Try again: "))
elif (userNumber == RNG):
    print("You got it right! Congrats!")

    # Third chance.

if (userNumber > RNG):
    print("It's smaller.")
    userNumber = int(input("Try again: "))
elif (userNumber < RNG):
    print("It's bigger.")
    userNumber = int(input("Try again: "))
elif (userNumber == RNG):
    print("You got it right! Congrats!")

    # Fourth chance.

if (userNumber > RNG):
    print("It's smaller.")
    userNumber = int(input("Try again: "))
elif (userNumber < RNG):
    print("It's bigger.")
    userNumber = int(input("Try again: "))
elif (userNumber == RNG):
    print("You got it right! Congrats!")

    # Fifth chance.

if (userNumber > RNG):
    print("It's smaller.")
    userNumber = int(input("Try again: "))
elif (userNumber < RNG):
    print("It's bigger.")
    userNumber = int(input("Try again: "))
elif (userNumber == RNG):
    print("You got it right! Congrats!")

    
if (userNumber > RNG):
    print("It's smaller.")
    print("You lost")
    print("It was " + RNG + ".")
elif (userNumber < RNG):
    print("It's bigger.")
    print("You lost!")
    print("It was " + str(RNG) + ".")