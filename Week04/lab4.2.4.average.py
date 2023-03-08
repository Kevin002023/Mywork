# average.py
# Author: Kevin
# Ask the user for a number continuously until they enter a 0 at which point the code lists the numbers selected and averages them

numbers = []

x = int(input("Please enter number: "))
while x != 0:
    numbers.append(x)
    x= int(input("Enter another number (0 to quit): " ))

print(numbers)
average = (sum(numbers)) / len(numbers)
print("The average is:", average)