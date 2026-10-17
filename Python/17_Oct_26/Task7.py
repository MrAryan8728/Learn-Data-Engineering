"""
Task 7
Given:
text = "  Google Ads Data Pipeline  "
Do:
1. Remove leading/trailing spaces.
2. Convert to lowercase.
3. Count the number of characters.
4. Split it into words.
5. Replace "Google Ads" with "Meta Ads".
"""
text = "  Google Ads Data Pipeline  "
print(f"Original string is: {text}")

print("Task_1: Remove leading/trailing spaces.")
print(text.strip())

print("Task_2: Convert to lowercase.")
print(text.lower())

print("Task_3: Count the number of characters.")
print(len(text))

print("Task_4: Split it into words.")
print(text.split(" "))

print("Task_5: Replace Google Ads with Meta Ads.")
print(text.replace("Google Ads", "Meta Ads"))