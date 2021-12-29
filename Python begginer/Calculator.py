# Start

from typing import Literal

print("Here is a list of all available operations: + - * - Average - Percentage - - - /")

# Inputs

num1 = int(input("Input a number: "))

num2 = int(input("Input a second number: "))

Operation = input("Input a operation you want: ")

# Calculating

if (Operation == "+"):
    print(num1 + num2)

elif (Operation == "X" or Operation == "x" or Operation == "*"):
    print(num1 * num2)

elif (Operation == "/"):
    print(num1 / num2)

elif (Operation == "Avg" or Operation == "Average"):
    print(num1 + num2 / 2)

elif (Operation == "Per" or Operation == "Percentage"):
    print(num1 / num2 * 100)

elif (Operation == "-"):
    print(num1 - num2)

