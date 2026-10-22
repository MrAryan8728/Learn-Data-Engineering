"""
Task 2: 
Create:
1. A list containing the names of only Data employees
Expected:
["A", "B", "D"]

2. A list containing salaries greater than 10
Expected:
[12, 15]

3. A dictionary mapping employee name → salary for Data employees
Expected:
{    
    "A": 8,
    "B": 12,
    "D": 15
}

"""
employees = [
    {"name": "A", "salary": 8, "department": "Data"},
    {"name": "B", "salary": 12, "department": "Data"},
    {"name": "C", "salary": 6, "department": "IT"},
    {"name": "D", "salary": 15, "department": "Data"},
    {"name": "E", "salary": 5, "department": "HR"}
]

only_data_emp = [employee["name"] for employee in employees if employee["department"] == 'Data']
greater_than_10 = [employee["salary"] for employee in employees if employee["salary"] > 10]
dict_emp_name_sal = {employee["name"]: employee["salary"] for employee in employees if employee["department"] == 'Data'}
print(f"{only_data_emp}\n{greater_than_10}\n{dict_emp_name_sal}")