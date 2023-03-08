# student_data.py
# Author: Kevin
# store a students name, their courses and frades ina  dict. hte program should then print out her data

student = {
    "name": "Mary",
    "courses" : [
        {
            "coursename" : "History",
            "grade" : 99
        },
        {
            "coursename" : "Programming",
            "grade" : 45
        }
    ]
}

print("Student: {}" .format(student["name"]))
for course in student["courses"]:
    print("\t {} \t: {}".format(course["coursename"], course["grade"]))