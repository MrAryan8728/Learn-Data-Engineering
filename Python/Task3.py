"""
Given:
numbers = [10, 25, 30, 45, 50, 65, 70]

Write code to:
1. Print every number.
2. Print only even numbers.
3. Print only numbers greater than 40.
4. Calculate the sum.
5. Find the maximum number.
6. Count how many numbers are greater than 40.
Don't use sum() or max() for #4 and #5 initially.
"""
numbers = [10, 25, 30, 45, 50, 65, 70]

print("Task: Every number in the list.")
for num in numbers:
    print(num, end=", ")

print("\nTask: Only even numbers.")
for num in numbers:
    if num % 2 == 0:
        print(num, end = ", ")

print("\nTask: Numbers greater than 40.")
for num in numbers:
    if num > 40:
        print(num, end = ", ")

print("\nTask: Sum of the numbers.")
sum = 0
for num in numbers:
    sum += num
print(f"Sum of all numbers are: {sum}")

print("\nTask: Find the maximum number.")
mx = -1
for num in numbers:
    if num > mx:
        mx = num
print(f"Max number in array is: {mx}")

print("\nCount of numbers greater than 40.")
count = 0
for num in numbers:
    if num > 40:
        count += 1
print(f"Count is : {count}")
print("Done. ")