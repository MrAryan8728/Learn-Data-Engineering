"""
Create:
def calculate_average_salary(employees):

Input:
employees = [
    {"name": "A", "salary": "8"},    
    {"name": "B", "salary": "12"},    
    {"name": "C", "salary": "INVALID"},    
    {"name": "D", "salary": "15"},    
    {"name": "E", "salary": "N/A"}
]


Your function must:
1. Convert salary to int.
2. Calculate the average using only valid salaries.
3. Skip invalid salary records.
4. Print the name of each skipped employee.
5. Return the average salary.
6. Handle the case where there are zero valid salaries.
Expected valid average:
11.67

Important
Don't use a broad:
except:

Use the appropriate exception.
"""
employees = [
    {"name": "A", "salary": "8"},    
    {"name": "B", "salary": "12"},    
    {"name": "C", "salary": "INVALID"},    
    {"name": "D", "salary": "15"},    
    {"name": "E", "salary": "N/A"}
]
def calculate_average_salary(employees):
    total_salary, valid_count = 0, 0
    for employee in employees:
        try:
            total_salary += int(employee['salary'])
            valid_count += 1
        except ValueError:
            print(f"Invalid salary for: {employee['name']}")
    if valid_count == 0:
        print("No valid salary is present!")
        return
    return round(total_salary/valid_count, 2)

res = calculate_average_salary(employees)
print(f"Average salary for employees are: {res}")


    
    