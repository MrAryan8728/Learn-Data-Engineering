"""
Input API
https://jsonplaceholder.typicode.com/posts

Your functions
Create these 3 functions:
1. fetch_page(page, limit)
- Call the API.
- Send _page and _limit.
- If successful → return JSON data.
- If failed → return None.
2. transform_records(records)

Convert:
{    
    "userId": 1,    
    "id": 1,    
    "title": "some title",    
    "body": "..."
}

into:
{
    "id": 1,    
    "user_id": 1,    
    "title": "some title"
}


Return the transformed list.
3. save_to_json(records, filename)
Save the records using json.dump().
Main program
Use those functions to:

Fetch 3 pages
     ↓
Transform each page
     ↓
Combine into one list
     ↓
Save → posts_output.json

At the end print:
Total records: 30
ETL completed successfully!

Important
If any page fails, stop the pipeline and do not claim ETL completed successfully.
"""
import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"
all_pass = True
def fetch_page(page, limit):
    data = []
    for pg in range(1, page + 1):
        params = {
            "_page":pg,
            "_limit":limit
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data.extend(response.json()) 
        else:
            all_pass = False
            print("API request failed.")

    return data

def transform_records(records):
    flatten_data = []
    for row in records:
        flatten_data.append(
            {
                "id":row['id'],
                "user_id":row['userId'],
                "title":row['title']
            }
        )
    return flatten_data

def save_to_json(records, filename):
    with open(filename, 'w') as file:
        json.dump(records, file, indent=4)
        print(f"File save with name: {filename}")

data = fetch_page(3, 10)
flat_data = transform_records(data)
save_to_json(flat_data, "posts_output.json")
print(f"Total records:{len(data)}")
if all_pass:
    print("ETL completed successfully!")