"""
Using csv.DictReader
Find:
1. Number of employees.
2. Employees with salary >= 8.
3. Average salary.
4. Highest-paid employee.
5. Number of Data Engineers.
"""
import csv

with open("employees.csv", "r") as file:
    reader = csv.DictReader(file)

    count = 0
    emp_high_sal = []
    sum = 0
    mx_sal = 0
    mx_pd_emp = ["Placeholder"]
    count_de = 0
    for row in reader:
        count += 1
        sal = int(row['salary'])
        sum += sal
        if row["role"] == 'Data Engineer':
            count_de += 1
        if sal > mx_sal:
            mx_sal = sal
            mx_pd_emp[0] = row
        if sal >= 8:
            emp_high_sal.append(row)
    print(f"1.Number of employees: {count}")
    print(f"\n2.Employees with salary >= 8: {emp_high_sal}")
    print(f"\n3.Average salary: {sum/count}")
    print(f"\n4.Highest paid employee: {mx_pd_emp}")
    print(f"\n5.Number of Data Engineers: {count_de}")