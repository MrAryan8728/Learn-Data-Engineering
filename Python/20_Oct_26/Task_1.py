"""
Task 1:
Write a small Python program using requests that:
1. Calls this public API:
   https://jsonplaceholder.typicode.com/users
2. Prints the HTTP status code.
3. Converts the response to JSON.
4. Prints the name and email of every user.
5. If the status code isn't 200, print "API request failed".
"""
import requests

url = "https://jsonplaceholder.typicode.com/users"
# calling API.
response = requests.get(url)
# print status code.
print(f"Response status: {response.status_code}")
# printing name and email only if ok.
if response.status_code == 200:
    # convert response to json.
    data = response.json()
    for row in data:
        print(row['name'] + " -> " + row['email'])
else:
    print("API request failed.")