import json

JSON_FILE_PATH = "data/PropertyRecords.json"

with open(JSON_FILE_PATH, "r", encoding="utf-8") as file:
    data = json.load(file)

# Print the first record's keys
print("🔍 Available Columns:", data[0].keys())
