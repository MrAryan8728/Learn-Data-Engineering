"""
Task 1:
Create a function:
process_employee_data(employees)

Input:
employees = [
    {"name": "A", "salary": 8, "department": "Data"},    {"name": "B", "salary": 12, "department": "Data"},    {"name": "C", "salary": 6, "department": "IT"},    {"name": "D", "salary": 15, "department": "Data"}
]

The function should:
1. Find the average salary.
2. Find the highest-paid employee.
3. Count employees in the Data department.
4. Return all three results.
Expected structure:
    {    
        "average_salary": ...,    
        "highest_paid": ...,    
        "data_employee_count": ...
    }

Important
Don't print the results inside the function.
The function should return the result, and outside the function you should do:
result = process_employee_data(employees)
print(result)
"""
employees = [
    {"name": "A", "salary": 8, "department": "Data"},
    {"name": "B", "salary": 12, "department": "Data"},
    {"name": "C", "salary": 6, "department": "IT"},
    {"name": "D", "salary": 15, "department": "Data"}
]
def process_employee_data(employees):
    sum, count, result, mx_sal, emp, count_data_dep = 0, 0, {}, 0, None, 0
    try:
        for employee in employees:
            if employee['department'] == 'Data':
                count_data_dep += 1
            salary = int(employee['salary'])
            if salary > mx_sal:
                mx_sal = salary
                emp = employee['name']
            sum += salary
            count += 1
        result["average_salary"] = sum/count
        result["highest_paid"] = emp
        result["data_employee_count"] = count_data_dep

    except ZeroDivisionError:
        print("Can't divide with zero.")
    except ValueError:
        print("Invalid salary.")

    return result

response = process_employee_data(employees)
print(response)