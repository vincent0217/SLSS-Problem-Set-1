# Quiz Creation Activity

import time
from rich import print

# Quiz has 5 questions the user will answer. It will keep track of score and give a final result.

score = 0

# Introduction
print("Welcome to the Qwiztown!!! \nHere you will be taught the basics to survive in school.")
time.sleep(1.5)
user_name = input("Print your user name: ")

print(f"Good luck {user_name}!\n")
time.sleep(1)

# 1. a number as an answer (e.g., What is 1+1?)
print("Your first task is to solve an elementary level math question.")
answer = input(f"What is 1 + 1: ")
if str(answer) == "2":
    print("Super!")
    score += 1
else:
    print("Better luck [bold black on white]next time[/bold black on white]!")
print("")
time.sleep(1)

# Transition
print("Are you ready for the next question? HERE WE GO!")
time.sleep(1.5)
print("")

# 2. text (e.g. What is Harry Potter's last name?)
initials = input(f"What is [/bold red]Michael Jordan's initials: ").lower().strip(".,?!")

if str(initials) == "mj":
    print(f"Fantastic!")
    score += 1
else:
    print(f"C'mon now")
print("")
time.sleep(1)

# Transition to question 3
print(f"Here comes question 3 {user_name}!")
time.sleep(1)

# 3. a selection (Which of these choices are correct? A, B, or C?)
answer = input(f"What is the colour of the sky? Select one of the options below.\n"
               f"\nA. Blue\nB. Red\nC. purple\n").lower().strip("!?.,")
a = "blue"
b = "red"
c = "purple"

if answer == a:
    print("Wow, you rock!")
    score += 1
elif answer == b:
    print("Dude, what kind of sky is red?")
else:
    print("say no more. We live in different universes.")
time.sleep(1)

print(f"Your total score is {score}.")
print(f"")