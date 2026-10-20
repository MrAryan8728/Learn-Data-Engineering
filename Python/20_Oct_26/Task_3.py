"""
Task 3:
Use this public API:
https://httpbin.org/headers

Write Python code that:
1. Creates a headers dictionary with:"X-Developer-Name": "Aryan""X-Project": "DataEngineering"
2. Sends a GET request using headers=headers.
3. Prints the status code.
4. Converts the response to JSON.
5. Prints the returned headers section.
"""
import requests

url = "https://httpbin.org/headers"
headers = {
    "X-Developer-Name": "Aryan",
    "X-Project": "DataEngineering"
}

response = requests.get(url, headers=headers)
print(f"Status code: {response.status_code}")

if response.status_code == 200:
    data = response.json()
    print(data['headers'])
else:
    print("API call failed!")