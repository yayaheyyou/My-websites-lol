# Welcome 

# Calculating right answers.

CorrectAnswers = 0

WrongAnswers = 0 

##################################################

print("Welcome to this EPIC quiz!")

# First question.

print("What is the water's chemical symbol?")

firstQuestion = input("Answer: ")

if (firstQuestion == "H2O"):
    print("Correct!")
    CorrectAnswers += 1

else:
    print("False!")
    WrongAnswers +=1

##################################################

# Second question.

print("Who was the first president of the usa?")

secondQuestion = input("Answer: ")

if (secondQuestion == "Goerge Washington"):
    print("Correct!")
    CorrectAnswers += 1

elif (secondQuestion != "Goerge Washington"):
    print("False!")
    WrongAnswers += 1

# Third question.

print("What's the quotient of 6 / 2?")

thirdQuestion = input("Answer: ")

if (thirdQuestion == "3"):
    CorrectAnswers += 1
    print("Correct!")

else:
    WrongAnswers += 1
    print("False!")

# Fourth question.

print("What's the pi rounded up to? (only 2 digits after the dot)")

fourthQuestion = input("Answer: ")

if (fourthQuestion == "3.17"):
    CorrectAnswers += 1
    print("Correct!")

else:
    WrongAnswers += 1
    print("False!")

##################################################

# Calculation.

print( "You got " + str(WrongAnswers) + " wrong answers.")
print("You got " + str(CorrectAnswers) + " correct answers.")