"""
Task 2: 
Use this API:
https://jsonplaceholder.typicode.com/posts

Write Python code that:
1. Sends userId = 1 as a parameter.
2. Gets the posts.
3. Prints the status code.
4. Prints the id and title of every returned post.
5. Print how many posts were returned.
Don't use the URL with ?userId=1 manually. Use params.
"""
import requests

url = "https://jsonplaceholder.typicode.com/posts"
params = {
    "userId": 1
}
count = 0

response = requests.get(url, params=params)
print(f"Response with code: {response.status_code}")
if response.status_code == 200:
    data = response.json()
    for row in data:
        count += 1
        print(str(row['id']) + "->" + row['title'])
    print(f"Total No. of Response: {count}")
else:
    print("API request failed!")