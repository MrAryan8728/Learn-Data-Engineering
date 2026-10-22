"""
Task 4:
Your requirements
1. Join df_emp and df_salary using employee_id.
2. Keep all employees, even if they don't have a salary record.
3. Find the employees whose salary is missing.
4. Replace missing salary with 0.

Hint: 
Merge = df_emp.merge(...)
.isna(), .fillna() for missing values
"""
import pandas as pd

employees = [
    {"employee_id": 1, "name": "A", "department": "Data"},
    {"employee_id": 2, "name": "B", "department": "IT"},
    {"employee_id": 3, "name": "C", "department": "Data"},
    {"employee_id": 4, "name": "D", "department": "HR"}
]

salary = [
    {"employee_id": 1, "salary": 8},
    {"employee_id": 2, "salary": 12},
    {"employee_id": 3, "salary": 15}
]

df_emp = pd.DataFrame(employees)
df_salary = pd.DataFrame(salary)
df_merged = df_emp.merge(df_salary, on = 'employee_id', how = 'left')
print(df_merged.isna())
df_merged = df_merged.fillna(0)
print(df_merged)