"""
Task 4:
Use:
https://httpbin.org/status/429

Write Python code that:
1. Sends a GET request.
2. Prints the status code.
3. If 200 → print "Success".
4. If 429 → print "Rate limit exceeded".
5. For any other status → print "API request failed".
"""
import requests

url = "https://httpbin.org/status/429"

response = requests.get(url)
status = response.status_code
print(f"Status code: {status}")

if status == 200:
    print("Success")
elif status == 429:
    print("Rate limit exceeded.")
else:
    print("API request failed.")