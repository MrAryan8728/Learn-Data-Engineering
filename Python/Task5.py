"""
Task 5
Given:
customers = [    {"id": 1, "name": "A", "salary": 50000},    {"id": 2, "name": "B", "salary": 70000},    {"id": 3, "name": "C", "salary": 45000},    {"id": 4, "name": "D", "salary": 90000}]
Write code to:
1. Print every customer's name.
2. Print customers earning > 50,000.
3. Calculate total salary.
4. Find the highest salary.
5. Find the customer with the highest salary.
"""
customers = [    {"id": 1, "name": "A", "salary": 50000},    {"id": 2, "name": "B", "salary": 70000},    {"id": 3, "name": "C", "salary": 45000},    {"id": 4, "name": "D", "salary": 90000}, {"id": 5, "name": "E", "salary": 90000}]

print(f"Original list: {customers}")

print("\nTask_1: Print every customer's name.")
for customer in customers:
    print(customer["name"], end = ', ')

print("\nTask_2: Print customers earning > 50000")
for customer in customers:
    if customer["salary"] > 50000:
        print(customer["salary"], end = ", ")

print("\nTask_3: Calcuate total salary.")
sum = 0
for customer in customers:
    sum += customer["salary"]
print(f"Total salary: {sum}.")

print("\nTask_4: Find highest salary.")
mx = -1
for customer in customers:
    if customer["salary"] > mx:
        mx = customer["salary"]
print(f"Maximum salary is : {mx}")

print("\nTask_5: Find customer with highest salary.")
for customer in customers:
    if customer["salary"] == mx:
        name = customer["name"]
        print(f"Customer with max salary is: {name}")

print("All task Done.")