# Quiz Creation Activity

import time

# Quiz has 5 questions the user will answer. It will keep track of score and give a final result.

score = 0
average_score = 0
num_question = 0

# Introduction
print("Welcome to the Qwiztown!!! \nHere you will be taught the basics to survive in school.")
time.sleep(1.5)
user_name = input("Print your user name: ")

print(f"Good luck {user_name}!\n")
time.sleep(1)

# 1. a number as an answer (e.g., What is 1+1?)
num_question += 1
print("Your first task is to solve an elementary level math question.")
answer = input(f"What is 1 + 1: ")
if str(answer) == "2":
    print("Super!")
    score += 1
else:
    print("Better luck next time!")
print("")
time.sleep(1)

# 2. text (e.g. What is Harry Potter's last name?)
num_question += 1
initials = input(f"What is Michael Jordan's initials: ").lower().strip(".,?!")
if str(initials) == "mj":
    print(f"Fantastic!")
    score += 1
else:
    print(f"C'mon now")
print("")
time.sleep(1)

# 3. a selection (Which of these choices are correct? A, B, or C?)
num_question += 1
answer = input(f"What is the colour of the sky? Select one of the options below.\n\nA. Blue\nB. Red\nC. purple\n").lower().strip("!?.,")
a = "blue"
b = "red"
c = "purple"

if answer == "a":
    print("Wow, you rock!")
    score += 1
elif answer == "b":
    print("Dude, what kind of sky is red?")
else:
    print("Noooooo. We live in different universes.")
time.sleep(1)
print("")

# Question 4
num_question += 1
answer = input(f"What coding language are we using right now?\n").lower().strip("!?.,")
if answer == "python":
    score += 1
    print("That's right!")
else:
    print("NO!")
time.sleep(1)
print("")

# Question 5
num_question += 1
answer = input("What month is Thanksgiving in?\n").lower().strip("!?.,")
if answer in ["october", "10"]:
    print("You know your stuff")
    score += 1
else:
    print("smh.")
time.sleep(1)
print("")

average_score = score / num_question * 100
# Ending
print(f"Congrats {user_name}! You have finished the quiz.")
print(f"Your total score and percentage correct are {score} and {average_score}%.")
print(f"")

# --------------------------------------------------------------------------
total_score = 0

questions = [
    ["What is (1 + 1)*3?",[6]]
    ["what is Michael Jordan's initials?",["mj"]]
    ["What is the colour of the sky?",[a]]
    ["What coding language are we using right now?",["Python"]]
    ["What month is Thanksgiving in?",[October]]
].lower().strip("!?.,")
score = 0
for question in questions:
    print(question[0])

