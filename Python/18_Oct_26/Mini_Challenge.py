"""
Extract: Read the JSON(campaigns.json)
Transform:
1. Add CPC = cost/clicks (Handing divided by zero.)
2. Add Performance : CPC < 3 -> "Good", 3-5 -> "Average", > 5 -> "Poor"
Load: Write records into processed_campaigns.json
"""

import json

processed_camp = []
with open("campaigns.json", "r") as file:
    data = json.load(file)

    for row in data:
        try:
            row["cpc"] = round(row["cost"]/row["clicks"], 3)
            val = row["cpc"]
            if val < 3:
                row["performance"] = "Good"
            elif val >= 3 and val <= 5:
                row["performance"] = "Average"
            else:
                row["performance"] = "Poor"
            processed_camp.append(row)
        except ZeroDivisionError:
            print(f"Invalid value !")

with open("processed_campaigns.json", "w") as file:
    json.dump(processed_camp, file, indent = 3)
    print("Processed file is ready!.")