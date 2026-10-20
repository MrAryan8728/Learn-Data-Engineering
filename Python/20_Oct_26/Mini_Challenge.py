"""
Use:
https://jsonplaceholder.typicode.com/posts

Requirements
Fetch 3 pages × 10 records.
For every record, create a transformed record containing only:
id
user_id
title

Rename userId → user_id.
Example:
{    "id": 1,    "user_id": 1,    "title": "..."}


Then:
1. Loop through 3 pages.
2. Send _page and _limit=10.
3. Handle non-200 responses.
4. Add the transformed records to one flat list.
5. Save the final 30 records to:
   posts_output.json
6. Use json.dump(..., indent=4).
7. Print:
   - records fetched per page
   - total records
   - "ETL completed successfully"
One extra DE requirement
Don't let one failed page silently produce an incomplete dataset.
If a page fails, print:
Page X failed

and stop the pipeline.
"""
import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"
transformed_response = []
success = True
for page in range(1, 4):
    params = {
        "_page": page,
        "_limit":10
    }
    response = requests.get(url, params = params)
    if response.status_code == 200:
        print(f"Records for page:{page} begins.")
        data = response.json()
        for row in data:
            temp = {
            "id": row['id'],
            "user_id" : row['userId'],
            "title" : row['title']
            }
            transformed_response.append(temp)
            print(f"{row['id']}-> {row['userId']}, {row['title']}")
    else:
        print("API Call failure!:(")
        # if any page fails
        print(f"Page: {page} failed")
        success = False
        break
print(f"Total Records: {len(transformed_response)}")
with open("posts_output.json", "w") as file:
    json.dump(transformed_response, file, indent=4)
    print("File saved successfully!")
if success:
    print("ETL completed successfully!")
else:
    print("ETL failed!")
