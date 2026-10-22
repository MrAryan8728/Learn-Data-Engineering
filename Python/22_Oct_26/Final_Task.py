"""
Task :
Build a small Pandas ETL pipeline:
Extract
Create a DataFrame from employees.
Transform
1. Create annual_salary = salary * 100000
2. Create salary_level:
   - salary >= 12 → "High"
   - salary >= 8 → "Medium"
   - otherwise → "Low"
3. Keep only employees with salary >= 8
4. Create a department summary containing:
   - avg_salary
   - max_salary
   - employee_count
Load
Save the final department summary to:
department_summary.csv

Use:
.to_csv(...)

Important
Don't worry about making it production-grade. I want to see whether you can combine:
"""
import pandas as pd
import numpy as np

employees = [
    {"employee_id": 1, "name": "A", "department": "Data", "salary": 8},
    {"employee_id": 2, "name": "B", "department": "Data", "salary": 12},
    {"employee_id": 3, "name": "C", "department": "IT", "salary": 6},
    {"employee_id": 4, "name": "D", "department": "IT", "salary": 10},
    {"employee_id": 5, "name": "E", "department": "Data", "salary": 15},
    {"employee_id": 6, "name": "F", "department": "HR", "salary": 5}
]
#Extract
df = pd.DataFrame(employees)

#Transform
df['annual_salary'] = df['salary']*100000

cases = [
    df['salary'] >= 12,
    df['salary'] >= 8
]

value = [
    "High",
    "Medium"
]

df['salary_level'] = np.select(cases, value, default = 'Low')
df = df[df["salary"] >= 8]

filtered_data = df.groupby('department').agg(
    avg_salary = ("salary", "mean"),
    max_salary = ("salary", "max"),
    employee_count = ("name", "count")
)

filtered_data.to_csv("department_summary.csv", index = False)
print("ETL completed successfully.")
