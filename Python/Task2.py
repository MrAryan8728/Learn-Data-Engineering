"""
Task 2:
Write a program that takes a salary and prints:
< 5   → "Low"
5 – 10   → "Medium"
10 – 15  → "Good"
> 15   → "Excellent"
Then modify it so that 10 LPA or more prints: ("Ready to switch")
"""

sal = int(input("Enter your salary(in LPA): "))
if sal < 5:
  print("Low")
elif sal >5 and sal <= 10:
#  print("Medium")
   print("Ready to switch")
elif sal > 10 and sal <= 15:
 print("Good")
else:
 print("Excellent")
print("Thanks for info!. Wish you get 100% hike.")