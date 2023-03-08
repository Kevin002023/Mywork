# random_generator.py
# Author: Kevin
# generates a random number between 1 and 10

import random
# Extra - changed the program so the user inputs the range limits

lowlim= int(input("Insert Lower Range limit here: "))
highlim= int(input("Insert Higher Range Limit here: "))
number = random.randint(lowlim, highlim)

print("Here is a random number {}" .format(number))

