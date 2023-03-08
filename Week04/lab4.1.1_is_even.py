# is_even.property
# Author: Kevin 
# Prompt the user to input an integer and have the code output if it is even or odd


a = int(input("Please insert a number here: "))

while a != -1:
    if (a%2 == 0):
       print(f"{a} is an even number")
    else:
        print(f"{a} is an odd number")
    a = int(input("Please insert a number here: "))
print("Finished")
