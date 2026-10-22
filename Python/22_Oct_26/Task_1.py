"""
Task 1:
Using the 5-employee dataset I gave you above, write code to:
1. Create the DataFrame.
2. Print df.
3. Print df.shape.
4. Print name and salary.
5. Print employees with salary > 10.
6. Print average salary.
"""

import pandas as pd

employees = [
    {"name": "A", "salary": 8, "department": "Data"},
    {"name": "B", "salary": 12, "department": "Data"},
    {"name": "C", "salary": 6, "department": "IT"}
]
df= pd.DataFrame(employees)

print(df)

print(df.shape)

print(df[['name', 'salary']])

print(df[df['salary'] > 10])

print(round(df['salary'].mean(), 2))