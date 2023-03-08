# div.py
# Author: Kevin
# takes two inputs and divides the first by the second, ouptutting an interger and remainder

a = int(input("Insert number here: "))
b = int(input("Insert second number here: "))

c = int(a/b)
d = a%b

print("{} divided by {} equals {} and {} remaining" .format(a, b, c, d,))