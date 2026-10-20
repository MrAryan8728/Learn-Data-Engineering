"""
Task 5:
Use:
https://jsonplaceholder.typicode.com/posts

Your task
Write Python code that:
1. Uses page and limit parameters.
2. Fetches 10 records per page.
3. Fetches 3 pages.
4. Collects all records into one list.
5. Prints:
   - Number of records fetched from each page
   - Total records
   - id and title of all records
Hint:
params = {    "_page": page,    "_limit": 10}

Use a for loop for the 3 pages.
"""
import requests

url = "https://jsonplaceholder.typicode.com/posts"
combined_records = []
for page in range(1, 4):
    params = {
        "_page":page,
        "_limit":10
    }

    response = requests.get(url, params = params)

    if response.status_code == 200:
        data = response.json()
        combined_records.extend(data)
        print(f"Number of record in page {page} is {len(data)}")
        for record in data:
            print(f"{record['id']} -> {record['title']}")
        print(f"End of page {page} records.")

    else:
        print("API call failed!")
print(f"Total records: {len(combined_records)}")