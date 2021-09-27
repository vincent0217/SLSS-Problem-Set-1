# Quiz Creation Activity

import time

# Quiz has 5 questions the user will answer. It will keep track of score and give a final result.

# Introduction
print("Welcome to the Qwiztown!!! \nHere you will be taught the basics to survive in school.")
time.sleep(1.5)
print("Good luck.")
time.sleep(2)

# 1. a number as an answer (e.g., What is 1+1?)
print("Your first task is to solve an elementary level math question.")
answer = input(f"What is 1 + 1: ")
if int(answer) == 2:
    print("Super!")
else:
    print("Better luck next time!")