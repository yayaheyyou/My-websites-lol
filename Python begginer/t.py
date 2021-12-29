# Modules

import random
import math

# The start 

print("Welcome to Guess the number!")
print("In this game you guess numbers based on if they are bigger or smaller.")
print("The numbers range from 1 to 100.")

# Some vars. 

userNumber = int(input("Write your guess: "))

RNG = random.randint(1, 100)

while userNumber != RNG:
    print("Try again!")
    userNumber = int(input("Try again: "))
    if (userNumber < RNG):
        print("The number is bigger!")
        userNumber = int(input("Try again: "))
    if (userNumber > RNG):
        print("The number is smaller!")
        userNumber = int(input("ry again: "))
    if (userNumber == RNG):
        print("You won!")
        print(f"It was indeed {RNG}.")