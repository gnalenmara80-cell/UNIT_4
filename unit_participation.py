"""
Programme name: unit_participation.py
Author: Gnalen Mara
Purpose: this programme use list comprehension to create a list of 100 random integers between 1 to 10
Starter code: None
Date: 02/06/2026
"""
import random
# this will create a list of 100 random integers between 1 and 10
random_list = [random.randint(1, 10) for _ in range(100)]
# this will output the total number of integers in the list
print("Total elements:", len(random_list))
# this will print the sum of all numbers in the list
print("Sum:", sum(random_list))
# this will print the average of the numbers in the list
print("Average:", sum(random_list) / len(random_list))