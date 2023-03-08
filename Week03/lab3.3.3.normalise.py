# normalise.py
# Author: Kevin
# converts a string to lowercase, removes any leading or trailing spaces and outputs the length of the input and output strings

string= input("insert phrase here: ")
lcstring = string.casefold()

no_leading = lcstring.strip()
length1 = len(string)
length2 = len(no_leading)
print("The string normalised is: " + no_leading)
print ("We have reduced the length of the string from {} to {}" .format(length1, length2))
