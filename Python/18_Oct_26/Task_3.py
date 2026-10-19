"""
Write Python to find:
1.Total clicks.
2.Total cost.
3.Campaign with highest clicks.
4.Total cost per customer.
Expected conceptually:
101 → 1400.50
102 → 800
103 → 300
5.Create a new JSON file: high_click_campaigns.json
containing campaigns where:
clicks >= 150
"""

import json

high_click_campaigns = []
with open("campaigns.json", "r+") as file:
    data = json.load(file)
    clicks, cost, mx_clicks, cmp_mx_clicks = 0, 0, 0, None
    cost_per_customer = {}
    for row in data:
        clicks += row['clicks']
        cost += row['cost']
        if row['clicks'] >= 150:
            high_click_campaigns.append(row)
        if row['clicks'] > mx_clicks:
            mx_clicks = row['clicks']
            cmp_mx_clicks = row
        cost_per_customer[row['customer_id']] = cost_per_customer.get(row['customer_id'], 0) + row['cost']

    print(f"1. Total clicks: {clicks}\n")
    print(f"2. Total cost: {cost}\n")
    print(f"3. Campaign with highest clicks: {cmp_mx_clicks}\n")
    print(f"4. Total cost per customer: {cost_per_customer}\n")
    print(f"5. New file created with name: high_click_campaigns.json")
    
with open("high_click_campaigns.json", "w") as file:
    json.dump(high_click_campaigns, file, indent=3)