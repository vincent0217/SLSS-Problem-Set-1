# Quiz Creation Activity

import time

# Quiz has 5 questions the user will answer. It will keep track of score and give a final result.

# Introduction
print("Welcome to the Qwiztown!!! \nHere you will be taught the basics to survive in school.")
time.sleep(1.5)
user_name = input("Print your user name: ")

print(f"Good luck {user_name}!\n")
time.sleep(2)

# 1. a number as an answer (e.g., What is 1+1?)
print("Your first task is to solve an elementary level math question.")
answer = input(f"What is 1 + 1: ")
if int(answer) == 2:
    print("Super!")
else:
    print("Better luck next time!")
print("")
time.sleep(1.5)

# Transition
print("Are you ready for the next question? HERE WE GO!")
time.sleep(1.5)
print("")

# 2. text (e.g. What is Harry Potter's last name?)
initials = input(f"What is Michael Jordan's initials: ").lower().strip(".,?!")

if str(initials) == "mj":
    print(f"Fantastic!")
else:
    print(f"C'mon now")
print("")
