def extract(file_path):
    import json
    with open(file_path, 'r') as f:
        data = json.load(f)
    # Check the first item in the data to confirm all fields are available
    print(data[0])  # Print the first record to check its structure
    return data
