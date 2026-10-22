"""
Task 2:
Filtering + Creating Columns

Using the same df, do these:
1. Create a new column annual_salary:
   salary × 100000
   So, 8 becomes 800000.
2. Create a new column salary_level:
   - salary >= 12 → "High"
   - salary >= 8 → "Medium"
   - otherwise → "Low"
3. Display only:
   name, salary, annual_salary, salary_level

Hint: You can create a column directly with Pandas. For salary_level, try using np.where or np.select
"""

import pandas as pd
import numpy as np

employees = [
    {"name": "A", "salary": 8, "department": "Data"},
    {"name": "B", "salary": 12, "department": "Data"},
    {"name": "C", "salary": 6, "department": "IT"}
]

df = pd.DataFrame(employees)
df['annual_salary'] = df['salary']*100000

conditions = [
    df['salary'] >= 12,
    df['salary'] >= 8
]
choices = [
    "High",
    "Medium"
]
df['salary_level'] = np.select(conditions, choices, default = 'Low')

print(df[['name', 'salary', 'annual_salary', 'salary_level']])