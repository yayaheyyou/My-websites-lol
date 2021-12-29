
import random 

# The start

print("Welcome to Guess the color!")

# The begin

Guess = str(input("Input your guess: "))

Words = ["Red", "Green", "Yellow"]

RWG = ''.join(random.choice(Words) for i in range(1)) 

# Conditioning 

if (Guess == RWG):
    print("You won!")

elif (Guess != RWG):
    print("You lost!")
    print("It was " + RWG + ".")

# The end


