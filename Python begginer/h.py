# Beginging the convo.
print("Hello!")

# First question.

print("What's your name?")

userName = str(input("My name is: "))

print("Oh hi " + userName + ", Nice to meet you!")

# Second question.

userHobby = input("What are your hobbies: ")

print("Yeah " + userHobby + " is cool, I should probably learn " + userHobby + ".")

# Third question.

userJob = input("What is your job: ")

print("That's awesome! You should be proud " + userName + ".")

# Switching cases using the "if" statement.

if (userJob == "Nothing"):
    print("That's okay, Don't be ashamed, You're still awesome!")

# Getting the user's age

userAge = int(input("How old are you: "))

if (userAge > 18):
 print("Good to know that im talking to a adult haha!")

elif (userAge < 18):
    print("I guess im talking to a minor...")

# More stuff in the convo.

y = print("Ask me any question: ")

x = input("")

# Switching in different cases

if (x == "What's your name?"):
 print("My name is yaya's AI!")

elif (x == "How old are you?"):
    print("I am 2 months old!")

elif (x == "What's your job?"):
    print("I talk with people!")

elif (x == ""): 
    print("Please enter a valid question next time, The following list displays them: What's your name?, How old are you?, What's your job?")

else:
    print("Enter a valid question next time!")
# Continuing the convo

input1 = print("What do you think about me?")

input2 = input("")

if (input2 == "You're a amazing bot!"):
 print("Thanks :)")

elif (input2 == "You're a decent bot."):
    print("Okay thanks, i guess :)")

elif (input2 == "You're a bad bot!"):
    print("Well then why wouldn't you go and jump off a cliff will ya bud?")

# Gathering the information collected.

print("Your name is " + userName + ".")

print("You're " + str(userAge) + " years old.")

print("You like " + userHobby + ".")



