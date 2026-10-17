"""
Task 4
Given:
customers = ["A", "B", "C", "D", "E"]
Do the following:
1. Add "F".
2. Remove "C".
3. Print the first customer.
4. Print the last customer.
5. Print the first three customers.
6. Sort the list.
7. Reverse the list.
"""
customers = ["A", "B", "C", "D", "E"]
print(f"Original list : {customers}")

print("\nTask: Add \"F\"")
customers.append("F")
print(customers)

print("\nTask: Remove \"C\"")
customers.remove("C")
print(customers)

print("\nTask: Print first customer")
print(customers[0])

print("\nTask: Print first three customers")
print(customers[0:3])

print("\nTask: Sort the list.")
print(sorted(customers))

print("\nTask: Reverse the list.")
n = len(customers)
print(f"Before: {customers}")
print(f"After: {customers[::-1]}")

print("All Task Done.")