# guess1.py
# Author: Kevin
# prompt the user to guess a number and keep prompting until the correct number is chose

a = 5

x = int(input("Please guess a number: "))
while x != a:
    print("Incorrect!")
    x = int(input("Guess again: "))
    
print("Well done the number was ", a)
