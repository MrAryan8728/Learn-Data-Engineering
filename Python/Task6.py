"""
Task 6
Given:
ids = [101, 102, 101, 103, 102, 104, 105, 104]
Find:
- unique IDs
- number of unique IDs
- IDs appearing more than once
"""
ids = [101, 102, 101, 103, 102, 104, 105, 104]
print(f"Original ids : {ids}")

print("Task_1: Unique IDs.")
unique_ids = set(ids)
print(f"Unique ids: {unique_ids}")

print("Task_2: Number of Unique IDs.")
print(f"Number of unique ids: {len(unique_ids)}")

print("Task_3: IDs appearing more than once.")
mp = {}
for id in ids:
    mp[id] = mp.get(id, 0) + 1

for key, val in mp.items():
    if val > 1:
        print(f"ID : {key}", end = ", ")