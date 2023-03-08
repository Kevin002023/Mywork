# floor.py
# Author: Kevin
# takes in a float and outputs a rounded down int

import math

number_to_floor = float(input("Enter a float number here: "))
floored_number = math.floor(number_to_floor)
print(str(number_to_floor) +" floored is " + str(floored_number))
