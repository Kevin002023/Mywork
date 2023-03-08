# topthree.py
# Author: Kevin
# generate 10 random numbers (between 0-100), print them out then list the top 3.

import random

how_many = 10
top_howmany = 3
min = 0
max = 100
numbers = []

for i in range(0,how_many):
    numbers.append(random.randint(min,max))
print(f"{how_many} random numbers:\t {numbers}")

top_ones = numbers.copy()

top_ones.sort(reverse = True)
print(f"The top {top_howmany} are \t\t {top_ones[0:top_howmany]}")