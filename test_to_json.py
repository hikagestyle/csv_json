import csv
import json

csv_name = "test.csv"
json_name = "test.json"

with open(csv_name, 'r', encoding="utf-8") as f:
    d_reader = csv.DictReader(f)
    d_list = [row for row in d_reader]

with open(json_name, 'w') as f:
    json.dump(d_list, f, ensure_ascii=False, indent=2)

# python3 test_to_json.py
