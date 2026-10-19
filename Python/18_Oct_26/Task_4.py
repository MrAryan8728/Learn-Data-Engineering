"""
Read bad_data
Your program should:
- process valid salaries
- identify invalid salaries
- NOT crash
- calculate the average of valid salaries

Expected:
Invalid salary: Amit
Invalid salary: Neha

Average valid salary: 8.33
"""
import csv

with open("bad_data.csv", "r") as file:
    reader = csv.DictReader(file)
    sum, count = 0, 0
    for row in reader:
        try:
            # print(f"{row['salary']} -> {type(int(row['salary']))}")
            sum += int(row['salary'])
            count += 1
        except:
            print(f"Invalid salary: {row['name']}")

    print(f"Average valid salary: {round(sum/count, 2)}")
