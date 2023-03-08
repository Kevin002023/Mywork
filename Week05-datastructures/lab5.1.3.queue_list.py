# queue_list.py
# Author: Kevin
# create a list(queue) output each number and remove it from the list.

import random

queue = []
number_of_numbers = 10
range_to = 100

for n in range(0, number_of_numbers):
    queue.append(random.randint(0, range_to))

print(f"The queue is {queue}")
 
while len(queue) != 0:
        current_number = queue.pop(0)
        print(f"current number is {current_number} and the queue is {queue}")

print("The Queue is now empty")
              