import pandas as pd

# Load the JSON data
df = pd.read_json("data/PropertyRecords.json")

# Display column names
print(df.columns)

# Show first few rows
print(df.head())
