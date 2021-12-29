# Modules:
import random 
from random import choice
from random import choices 
import math 
import typing 
from typing import Literal
from typing import Counter
import time
import os
import names
# Functions

def clearConsole():
    command = 'cls'
    os.system(command)

def randomName():
    name = names.get_first_name()
    print(name)

def randomFemaleName():
    name = names.get_first_name(gender="female")
    print(name)

def randomMaleName():
    name = names.get_first_name(gender="male")
    print(name)
# The start 




print("Welcome to the cave!")
print("In this story type game you will be able to change the story depending on your choices.")

storyGenre = input("What story genre do you prefer (scary, comedy or action.): ")

# Story genre conditions:


if (storyGenre == "scary" or storyGenre == "Scary"):
    print("OOO! Spooky, I see where you're coming from.")
    print("Well what story would you like it to be?")
    storyChoice1scary = input("(Like some character based story?)\nOr like some usual story with a random person's name?\nChoose from option 1 or 2: ")
else :
    print("die")

if (storyGenre == "comedy" or storyGenre == "Comedy"):
    storyChoice1comedy = input("Well well i like it!\nI actually quite like your taste.\nWell you're in for a treat!\nWhat do you want your story to be like?\nCharacter based or a random person's name\nChoose from option 1 or 2: ")

if (storyGenre == "action" or storyGenre == "Action"):
    storyChoice1action = input("Pew Pew am i right!\nWhat do you want your story to be?\nCharacter based or a random name's based?\nChoose from option 1 or 2: ")

    
# Choice 1 condition:


if (storyChoice1scary == "option 1" or storyChoice1scary == "1" or storyChoice1scary == "Option 1"):
    storyCharnamescary = input("What name do you want him/her/they to be: ")
    clearConsole()
    print("Me and my brother were at home.")
    time.sleep(1)
    print("We were home alone.")
    time.sleep(1)
    print(f"I heard a voice shouting my name ({storyCharnamescary})")
    time.sleep(1)
    print("The end.")

else :
    pass

if (storyChoice1scary == "option 2" or storyChoice1scary == "Option 2" or storyChoice1scary == "2"):
    clearConsole()
    name = names.get_first_name(gender="male")
    print("Me and my brother were at home.")
    time.sleep(1)
    print("We were home alone.")
    time.sleep(1)
    print(f"I heard a voice shouting my name ({name})")
    time.sleep(1)
    print("The end.")

else :
    pass

if (storyChoice1action == "1" or storyChoice1action == "option 1" or storyChoice1action == "Option 1"):
    storyCharnameaction = input("What name do you want him/her/they to be: ")
    clearConsole()
    print("Me and my brother were at home.")
    time.sleep(1)
    print("He shot a criminal.")
    time.sleep(1)
    print(f"The criminal's name was ({storyCharnameaction})")
    time.sleep(1)
    print("The end.")
    
else :
    pass

if (storyChoice1action == "2" or storyChoice1action == "option 2" or storyChoice1action == "Option 2"):
    clearConsole()
    name = names.get_first_name(gender="male")
    print("Me and my brother were at home.")
    time.sleep(1)
    print("He shot a criminal.")
    time.sleep(1)
    print(f"The criminal's name was ({name})")
    time.sleep(1)
    print("The end.")

else :
    pass

if (storyChoice1comedy == "1" or storyChoice1comedy == "option 1" or storyChoice1comedy == "Option 1"):
    storyCharnamecomedy = input("What name do you want him/her/they to be: ")
    clearConsole()
    print(f"Me and my brother were at home. My name is {storyCharnamescary}")
    time.sleep(1)
    print("He said a joke.")
    time.sleep(1)
    print(f"I laughed.")
    time.sleep(1)
    print("The end.")

if (storyChoice1comedy == "2" or storyChoice1comedy == "option 2" or storyChoice1comedy == "Option 2"):
    clearConsole()
    print("Me and my brother were at home.")
    time.sleep(1)
    print("He said a joke.")
    time.sleep(1)
    print(f"I laughed.")
    time.sleep(1)
    print("The end.")

else :
    pass

