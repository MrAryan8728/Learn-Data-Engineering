"""
Part 1:
Write Python code that:
1. Opens the file.
2. Reads its contents.
3. Prints the contents.
Then modify it to print one line at a time.

Part 2:
Read the file and print only employees whose salary >= 8 LPA.
"""
print("Part 1: Reading the file.")
with open("employees.txt", "r") as file:
    # data = file.read()
    # print(data)
    for line in file:
        print(line.strip())

print("\nPart 2: Applying filer of >= 8 LPA")
Data = []
with open("employees.txt", "r+") as file:
    for line in file:
        data = line.strip().split(",")
        if int(data[-1]) >= 8:
            print(','.join(data))
            Data.append(','.join(data))

print("\nPart 3: Creating new files for filtered data")
with open("high_salary_employees.txt", "w") as file:
    for val in Data:
        file.writelines(val + "\n")
    print("File created Successfully!")
