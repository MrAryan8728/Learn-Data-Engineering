"""
Task 8

def calculate_total(numbers):  

It should accept a list of numbers and return their total.

def find_even_numbers(numbers):

It should return a list containing only even numbers.
"""

def calculate_total(numbers):
    sum = 0
    for num in numbers:
        sum += num
    return sum

def find_even_numbers(numbers):
    lst = []
    for num in numbers:
        if num % 2 == 0:
            lst.append(num)
    return lst

num = [10, 20, 30, 40, 55, 60, 75]
print(f"Calling calculate_total: {calculate_total(num)}")
print(f"Calling find_even_numbers: {find_even_numbers(num)}")