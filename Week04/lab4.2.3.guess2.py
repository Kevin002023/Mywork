# guess2.py
# Author: Kevin
# # prompt the user to guess a number and keep prompting until the correct number is chose. Tell the user if the number is too high/low

import random

# had the code pick a random number
a = random.randint(0,101)


x = int(input("Please guess a number: "))
while x != a:
    if x > a:
        print("Incorrect, too high!")
    elif x < a:
        print("Incorrect, too low!")
    x = int(input("Guess again: "))
    
print("Well done the number was ", a)
