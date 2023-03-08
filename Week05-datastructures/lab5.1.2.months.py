# months.py
# author: Kevin
# creat a tuple that stores the months of the year. Then create another tuple that stores the summer months. print out the summer months

months = ("January",
            "Febraury",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December")

summer = months[4:7]
print(*summer, sep = "\n") # first way i did it. 

for month in summer:
    print(month)
