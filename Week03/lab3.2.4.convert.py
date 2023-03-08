# convert.py
# Author: Kevin
# take an input in dollars and cents and return an absolute amount in cents

number = float(input("Enter amount here: "))
absoluteValue = abs(number)

# 100 cents in a dollar. so to convert to cents multiply by 100

cents =(absoluteValue*100)
print(int(cents))