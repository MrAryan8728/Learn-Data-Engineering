"""
🔥 Day 1 Mini Challenge

You receive this data:

orders = [    {"customer": "A", "amount": 1200, "status": "completed"},    {"customer": "B", "amount": 800, "status": "pending"},    {"customer": "A", "amount": 1500, "status": "completed"},    {"customer": "C", "amount": 2000, "status": "completed"},    {"customer": "B", "amount": 700, "status": "completed"},]


Write a program that finds:
1.Total revenue from completed orders.
2.Number of completed orders.
3.Unique customers who placed completed orders.
4.Total completed-order revenue per customer.

Expected conceptual output:

Total Revenue: 5400
Completed Orders: 4
Customers: A, C, B

Revenue:
A → 2700
B → 700
C → 2000
"""

orders = [    {"customer": "A", "amount": 1200, "status": "completed"},    {"customer": "B", "amount": 800, "status": "pending"},    {"customer": "A", "amount": 1500, "status": "completed"},    {"customer": "C", "amount": 2000, "status": "completed"},    {"customer": "B", "amount": 700, "status": "completed"},]

print(f"Task_1: Total revenue from completed orders.")
revenue = 0
for order in orders:
    if order["status"] == "completed":
        revenue += order["amount"]

print(f"Total revenue: {revenue}\n=================")

print(f"Task_2: Number of completed orders.")
count = 0
for order in orders:
    if order["status"] == "completed":
        count += 1
print(f"Completed Orders: {count}\n===============")

print(f"Task_3: Unique customers who placed completed orders.")
lst = []
for order in orders:
    if order["status"] == "completed":
        lst.append(order["customer"])
print(f"Customers: {set(lst)}\n===============")

print(f"Task_4: Total completed-order revenue per customer.\nRevenue")
mp = {}
for order in orders:
    if order["customer"] in set(lst) and order["status"] == 'completed':
        mp[order['customer']] = mp.get(order['customer'], 0) + order['amount']

for key, value in mp.items():
    print(f"{key} -> {value}")
    

