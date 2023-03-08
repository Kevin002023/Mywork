# grade.py
# Author: Kevin
# Prompt user for input of percentage mark and outputs the corresponding grade

score = float(input("Please insert your percentage mark here: "))

if score<0 or score>100:
    print("Please enter a valid number between 0 and 100")
elif score<40:
    print("Fail")
elif score >=40 and score < 50:
    print("Pass")
elif score >= 50 and score < 60:
    print("Merit 2)")
elif score >=60 and score < 70:
    print("Merit 1")
elif score >= 70:
    print("Distinction")


# Extra: if we are to round percentages the code below shoudl work. eg. 39.5 = 40 = Pass
grade = round(score)
if grade<0 or grade>100:
    print("Please enter a valid number between 0 and 100")
elif grade<40:
    print("Fail")
elif grade >=40 and grade < 50:
    print("Pass")
elif grade >= 50 and grade < 60:
    print("Merit 2")
elif grade >=60 and grade < 70:
    print("Merit 1")
elif grade >= 70:
    print("Distinction")
