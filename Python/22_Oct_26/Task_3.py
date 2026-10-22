"""
Create a department-level summary containing:
1. Average salary per department
2. Maximum salary per department
3. Number of employees per department

department	avg_salary	max_salary	employee_count
Data	    11.67	        15	        3
IT	        8.00	        10	            2
"""

import pandas as pd

employees = [
    {"name": "A", "salary": 8, "department": "Data"},
    {"name": "B", "salary": 12, "department": "Data"},
    {"name": "C", "salary": 6, "department": "IT"},
    {"name": "D", "salary": 10, "department": "IT"},
    {"name": "E", "salary": 15, "department": "Data"}
]

df = pd.DataFrame(employees)

print(df.groupby("department").agg(
    avg_salary = ("salary", "mean"),
    max_salary = ("salary", "max"),
    employee_count = ("name", "count")
))